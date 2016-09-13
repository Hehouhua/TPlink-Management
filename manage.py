# -*- coding: cp936 -*-
import sys, getopt,time
import httplib
import urlparse
import re

import result
import config

def encodePara(val):
	#return urllib.urlencode(val)
	return val

class TPLink_Manage:
	def __init__( self , pwd , authInfoUrl , apiUrl , keyUrl):
		self.authInfoUrl=authInfoUrl
		self.apiUrl=apiUrl
		self.keyUrl=keyUrl
		self.url=''
		self.strde=''#从keyUrl来
		self.dict=''#从keyUrl来
		self.session=''	#this.session = this.securityEncode(authInfo[3], pwd, authInfo[4]);算出来的几分钟一变
		self.pwd = pwd
		self.encPwd=''#根据加密算法securityEncode(pwd, self.strDe, self.dic)算出来的，每次修改密码或者authinfo换了就用这个
		self.authInfo=[]#authInfo
		self.result=result.result()#认证结果
	
	def getAuthInfo(self):
		self.request(self.authInfoUrl, "GET")
		self.parseAuthRlt()
		
	def getKey(self):
		self.request(self.keyUrl, 'GET')
		self.strde = re.search('var\s+strDe\s+=\s+(.*?);', self.result.data, re.IGNORECASE).group(1)
		self.dict  = re.search('var\s+dic\s+=\s+([\s\S]*?);', self.result.data, re.IGNORECASE).group(1)
		
		self.strde=re.sub("[\"|\+|\s]","",self.strde)
		self.dict=re.sub("[\"|\+|\s]","",self.dict)
	
	def securityEncode(self , input1 , input2, input3):
		cl = 0xBB
		cr = 0xBB
		output=""
		len1 = len(input1)
		len2 = len(input2)
		lenDict = len(input3)
		length =len1 if(len1 > len2) else len2
		for i in range(0,length):
			if i<len1 and i<len2:
				cl = ord(input1[i])
				cr = ord(input2[i])
			else:
				cr = ord(input2[i]) if i >= len1 else 0xBB
				cl = ord(input1[i]) if i >= len2 else 0xBB
			output += input3[(cl ^ cr)%lenDict]
		return output
		
	def orgAuthPwd(self,pwd):
		return self.securityEncode(pwd, self.strde, self.dict);

	def initResult(self,rslt=''):
		self.result = result.result(rslt)
	
	def setLgPwd(self,pwd):
		#sessionLS.setItem(LGKEYSTR, pwd);
		self.encPwd = pwd;
	
	def auth(self,encPwd):
		self.getAuthInfo()
		time.sleep(1)
		self.session = self.securityEncode(self.authInfo[3], encPwd, self.authInfo[4])
		url  = self.apiUrl.replace("$CODE$",str(config.TDDP_AUTH)).replace("$ASYN$","0").replace("$ID$",encodePara(self.session))
		self.request(url, "POST")
		#self.parseAuthRlt()
		if config.ENONE == self.result.errorno:
			self.setLgPwd(encPwd)
		#return self.result

	def request(self , url , method='GET' , params='' , cookie=''):
		ret = urlparse.urlparse(url)    # Parse input URL
		if ret.scheme == 'http':
			conn = httplib.HTTPConnection(ret.netloc)
		elif ret.scheme == 'https':
			conn = httplib.HTTPSConnection(ret.netloc)
			
		url = ret.path
		if ret.query: url += '?' + ret.query
		if ret.fragment: url += '#' + ret.fragment
		if not url: url = '/'
		if method == 'GET':
			conn.request(method='GET', url=url , headers={'Cookie': cookie})
		else:
			conn.request(method='POST',url=url , body=params,headers={'Cookie': cookie,'Content-Type': 'application/x-www-form-urlencoded','Origin': 'http://192.168.1.1','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36','Referer': 'http://192.168.1.1/'})
		response = conn.getresponse()
		#给result赋值表示这次请求的状态
		self.result.data = response.read()
		self.result.headers = response.getheaders()
		self.result.errorno = config.EUNAUTH if response.status ==401 else config.ENONE
		if config.ENONE == self.result.errorno:
			#self.session=self.securityEncode(self.authInfo[3], self.encPwd, self.authInfo[4]) 
			print "Request ok!"
		if config.EUNAUTH == self.result.errorno:
			print "Request 401!"
			self.parseAuthRlt()
			self.session=self.securityEncode(self.authInfo[3], self.encPwd, self.authInfo[4]) 
		
			
			
	def parseAuthRlt(self):
		relCnt = self.result.data
		if relCnt.rfind("\r\n") == len(relCnt) - 2:
			relCnt = relCnt[0:len(relCnt) - 2]
		results = relCnt.split("\r\n");
		if not len(self.authInfo):
			print "Not Authed"
			#self.authInfo.append("")
			self.authInfo.append(results[0])
			self.authInfo.append(results[1])
			self.authInfo.append(results[2])
			self.authInfo.append(results[3])
			self.authInfo.append(results[4])
		if config.EUNAUTH == self.result.errorno :
			#self.authInfo[0] = ""
			self.authInfo[0] = results[0]
			self.authInfo[1] = results[1]
			self.authInfo[2] = results[2]
			self.authInfo[3] = results[3]
			self.authInfo[4] = results[4]
			print "Auth Failed"
			print self.authInfo[3]
			print self.authInfo[4]
		
	def lgDoSub(self):
		value=self.pwd
		if len(value) > 15 or len(value) < 6:
			print "password illegal"
		self.auth(self.orgAuthPwd(value))
		if self.result.errorno == config.ENONE:
			print "login success"
		else:
			print "login error"

	def reboot(self):
		url  = self.apiUrl.replace("$CODE$",str(config.TDDP_REBOOT)).replace("$ASYN$","0").replace("$ID$",encodePara(self.session))
		self.request(url, "POST")
		if config.EUNAUTH == self.result.errorno:
			print "认证已失效"
			return
		#print self.result.data
		
	def readStatus(self,status=13):
		url  = self.apiUrl.replace("$CODE$",str(config.TDDP_READ)).replace("$ASYN$","1").replace("$ID$",encodePara(self.session))
		self.request(url, "POST",str(status))
		if config.EUNAUTH == self.result.errorno:
			print "认证已失效"
			#return
		print self.result.data
		#print self.strde
		#print self.authInfo[3]
		#print self.authInfo[4]
	
	def manage(self):
		self.getKey()
		self.lgDoSub()
		#self.reboot()
		while True:
			break
			for i in range(38):
				self.readStatus(i)
				time.sleep(3)
		
def main():
	protocol='http://'
	host='192.168.1.1'
	authInfoUrl=protocol+host+'/common/Content.htm'
	apiUrl=protocol+host+'/?code=$CODE$&asyn=$ASYN$&id=$ID$'
	keyUrl=protocol+host+'/lib/Quary.js'
	
	console=TPLink_Manage("iiecas",authInfoUrl,apiUrl,keyUrl)
	console.manage()
	print "strde: ",console.strde
	print "dict: ",console.dict
	print "session: ",console.session
	print "encPwd: ",console.encPwd
	
if __name__ == "__main__":  
	main()