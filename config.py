## -*- coding: cp936 -*-
################################ from DM.js ################################
SYN = 0;
ASYN = 1;
TDDP_INSTRUCT = 0;
TDDP_WRITE = 1;		#/* 更新数据，对应于以前的SET命令； */
TDDP_READ = 2;		#/* 读取数据，对应于以前的GET命令； */
TDDP_UPLOAD = 3;	#/* 更新软件，由于在TDDPV3中，命令放到了数据中，因此"特殊子命令"字段可以去掉； */
TDDP_DOWNLOAD = 4;	#/* 备份软件配置。TDDPV2及其以前的意义将被覆盖。 */
TDDP_RESET =5;		#/* 恢复初始设置； */
TDDP_REBOOT = 6;	#/* 重启设备； */
TDDP_AUTH = 7;		#/* 认证 */
TDDP_GETPEERMAC = 8;	#/* 获取主机信息 */
TDDP_CONFIG = 9;	#/* 载入用户配置数据 */	
TDDP_CHGPWD = 10;	#/* 修改密码 */
TDDP_LOGOUT = 11;	#/* 登出 */

PARSE_INIT = 0;		#/* 初始态 */
PARSE_NOTE = 1;		#/* 以#开头的为注释。注意:只有在初始态遇到了#才认为会是注释，否则会被当作内容。 */
PARSE_CMD = 2;		#/* 解析命令。 */
PARSE_ID = 3;		#/* 解析数据块ID。 */
PARSE_INDEX = 4;	#/* 解析索引。 */
PARSE_VALUE = 5;	#/* 解析值。 */
PARSE_ERR = 6;		#/* 解析遇到错误。 */
					#CA1223 999-9131978274
					#CA1234 999-9131995435
					
######################### from error.js #####################################
EEXPT = -1;						#/* 异常情况 */
ENONE = 0;						#/* 没有错误 */
ENOMEMORY = 1;					#/* 内存不足 */
EINVARG = 2;					#/* 参数错误 */
EINVFMT = 3;					#/* 格式错误 */
EINVEVT = 4;					#/* 不支持的事件 */
EINVCODE = 5;				   #
EFORBID = 6;					#/* 禁止的操作。 */
EUNAUTH = 7;					#/* 认证失败。 */
EOVERFLOW = 8;				  #
EINVINSTRUCT = 9;				#/* 不支持的指令 */
EMD5 = 10;						#/* MD5校验失败 */
EDESENCODE = 11;				#/* DES加密失败 */
EDESDECODE = 12;				#/* DES解密失败 */
ECHIPID = 13;					#/* 不支持的芯片类型； */
EFLASHID = 14;					#/* 不支持的FLASH类型； */
EPRODID = 15;					#/* 不支持的产品型号； */
ELANGID = 16;					#/* 不支持的语言； */
ESUBVER = 17;					#/* 不支持子版本号； */
EOEMID = 18;					#/* 不支持的OEM类型； */
ECOUNTRYID = 19;				#/* 不支持的国家； */
ECODE = 20;						#/* 不支持的操作类型； */
EWANTYPE = 21;					#/* 不支持的WAN口接入类型； */
ETOOLONG = 22;					#/* 数据过长。 */
ESYSTEM = 23;					#/* 系统错误。 */
ENOECHO = 24;					#/* 超时无响应。 */
ENODEVICE = 25;					#/* 找不到设备。 */
EINVIP = 26;					#/* IP地址不正确。 */
EINVMASK = 27;					#/* 掩码不正确。 */
EINVGTW = 28;					#/* 网关不正确。 */
EINVIPMASKPAIR = 29;			#/* IP和掩码不匹配。 */
EGTWUNREACH = 30;				#/* 网关不可达。 */
EINVMTU = 31;					#/* MTU错误 */
EINVMACFMT = 32;				#/* MAC地址格式不正确。 */
EENTRYEXIST = 33;				#/* 条目已存在。 */
EENTRYNOTEXIST = 34;			#/* 条目不存在。 */
EENTRYCONFLIC = 35;				#/* 条目冲突。 */
ETABLEFULL = 36;				#/* 表满。 */
ETABLEEMPTY = 37;				#/* 空表。 */
EINVPORT = 38;					#/* 超出端口范围*/
EPORTRESERVED = 39;				#/* 端口冲突*/
EINVPTC = 40;					#/* 不支持的协议类型。 */
ECOMFLICTNET = 41;				#/* 网段冲突*/
EINVNET = 42;					#/* 非法的网段 */
EINVTYPE = 43;					#/* 非法的类型。 */
EINVMODE = 44;					#/* 非法的模式。 */
EINVTIME = 45;				  #
EINVFDNSVR = 46;				#/* 非法的首选DNS */
EINVSDNSVR = 47;				#/* 非法的备选DNS */
EINVDATA = 48;					#/* 数据合法性验证失败 */
EINVLEASETIME = 49;				#/* 非法的地址租期。 */
EINVADDRPOOL = 50;				#/* 非法的地址池。 */
EINVDATE = 51;					#/* 日期输入错误 */
EINVTIMEZONE = 52;				#/* 时区输入错误 */
ENOLINK = 53; 					#/*WAN口未连接 */
ESYSBUSY = 54;					#/* 系统繁忙。 */
EINVNUM = 55;				   #
EINVSIZE = 56;				  #
EINVTIMEOUT = 57;			   #
EINVMETRIC = 58;				#
EINVINTERVAL = 59;				#/* 时间间隔输入错误 */
EINVBOOL = 69;					#/* 布尔类型的取值只能是0或者1 */
EINVSSIDLEN = 70;				#/* 无线SSID长度不合法 */
EINVSECAUTH = 71;				#/* 无线安全设置的认证类型错误 */
EINVWEPAUTH = 72;				#/* WEP认证类型错误 */
EINVRADIUSAUTH = 73;			#/* RADIUS认证类型错误 */
EINVPSKAUTH = 74;				#/* PSK认证类型错误 */
EINVCIPHER = 75;				#/* 加密算法错误 */
EINVRADIUSLEN = 76;				#/* radius密钥短语长度错误 */
EINVPSKLEN = 77;				#/* psk密钥短语错误 */
EINVGKUPINTVAL = 78;			#/* 组密钥更新周期错误 */
EINVWEPKEYTYPE = 79;			#/* WEP密钥类型错误 */
EINVWEPKEYIDX = 80;				#/* 默认WEP密钥索引错误 */
EINVWEPKEYLEN = 81;				#/* WEP密钥长度错误 */
EINVACLDESCLEN = 82;			#/* MAC地址过滤条目描述信息长度错误 */
EINVWPSPINLEN = 83;				#/* WPS PIN码长度错误 */
EINVAPMODE = 84;				#/* 无线设备工作模式错误 */
EINVWLSMODE = 85;				#/* 无线速率模式(bgn)错误 */
EINVREGIONIDX = 86;				#/* 无线国家码错误 */
EINVCHANWIDTH = 87;				#/* 频段带宽错误 */
EINVRTSTHRSHLD = 88;			#/* 无线RTS阈值错误 */
EINVFRAGTHRSHLD = 89;			#/* 无线分片阈值错误 */
EINVBCNINTVL = 90;				#/* 无线beacon间隔错误 */
EINVTXPWR = 91;					#/* 无线Tx功率错误 */
EINVDTIMINTVL = 92;				#/* 无线DTIM周期错误 */	
EINVWDSAUTH = 93;				#/* 无线WDS认证类型错误 */
EINVA34DETECT = 94;				#/* 3/4地址格式配置错误 */
EINVWLANPWD = 95;				#/* invalid pwd */
EINVHOSTNAMELEN = 96;			#/* hostname is null */
EINVSPEEDCFG = 97;				#/* guestNet 最大上传速度或最大下载速度配置错误 */
EINVTIMEOUTCFG = 98;			#/* guestNet 超时配置错误 */
EINVMACGROUP = 99;				#/* MAC地址为组播地址 */
ENAMEBLANK = 100;				#/* 用户名输入为空 */
EPWDBLANK = 101;				#/* 密码输入为空 */
EINVMACZERO = 102;				#/* MAC地址全零 */
EINVMACBROAD = 103;				#/* 广播地址的MAC地址 */
EHOSTNAMEEMP = 104;				#/* 受控主机名为空 */
EOBJNAMEEMP = 105;				#/* 访问目标名为空 */
EPLANNAMEEMP = 106;				#/* 日程计划名为空 */
EOBJDOMAINALLEMP = 107;			#/* 访问目标域名全为空 */
EREFERED = 108;					#/* 条目被关联了 */
EDELPARTIAL = 109;				#/* 只删除了部分条目 */
EDELNOTHING = 110;				#/* 一个条目都没有删除 */
ERSACHECK = 111;				#/* RSA校验错误 */
EINVLGPWDLEN = 112;				#/* 登录密码长度不合法 */
EINLGVALCHAR = 113;				#/* 登录密码含有非法字符 */
EINLGVALOLDSAME = 114;			#/* 新登录密码和旧登录密码一样 */
EINVNETID = 115;				#/* 网络号全0或者1 */
EINVHOSTID = 116;				#/* 主机号全0或者1 */
EOUTOFRANGE = 117;				#/* 超出范围 */
EINDOMAIN = 118;				#/* 非法的域名 */
ELACKCFGINFO = 119;				#/* 缺少必要的配置信息 */
EINVKEY = 120;					#/* 旧密码错误 */
EINVRMTPORT = 121;				#/* 远程管理端口超出范围*/
EILLEGALPORT = 122;				#/* 端口值非法 */
EINVNAMELEN = 123;				#/* 用户名长度超出范围 */
EINVPWDLEN = 124;				#/* 密码长度超出范围 */
EINVNAME = 125;					#/* 用户名非法 */
ENOTLANSUBNET = 126;			#/* 不是LAN网段IP */
EHOSTALLEMPTY = 127;			#/* 受控主机IP全为空 */
EOBJALLEMPTY = 128;				#/* 访问目标IP和端口全为空 */
EINVGROUPIP = 129;				#/* 组播的IP地址 */
EINVLOOPIP = 130;				#/* 回环的IP地址 */
EINVIPFMT = 131;				#/* IP地址格式错误 */
ENOTLANWANNET = 132;			#/* 网段不是LAN或WAN */
ELANSUBNET = 133;				#/* LAN网段IP */
EINVPWD = 134;					#/* 密码非法 */
EIPRESERVED = 135;				#/* IP地址被占用 */
EINVPORTFMT = 136;				#/* 端口格式错误 */

################################## from model.js  ############################################
DEVICE_DATA_ID =  0 ;
SYSTEM_DATA_ID =  1 ;
SYSTEM_LOG_DATA_ID =  2 ;
EXCEPT_LOG_DATA_ID =  3 ;
LAN_DATA_ID =  4 ;
LCLPORT_DATA_ID =  5 ;
LCLHOST_DATA_ID =  6 ;
RMTHOST_DATA_ID =  7 ;
DHCPS_DATA_ID =  8 ;
DHCPS_LEASE_DATA_ID =  9 ;
TPDOMAIN_DATA_ID =  10 ;
FACTORY_DATA_ID =  11 ;
STACTRLTBL_DATA_ID =  12;
STARTTABLE_DATA_ID =  13 ;
STATIC_ROUTE_DATA_ID =  14 ;
DYNAMIC_ROUTE_DATA_ID =  15 ;
SYSTEM_ROUTE_DATA_ID =  16 ;
NAPT_ALG_DATA_ID =  17 ;
NAPT_DMZ_DATA_ID =  18 ;
NAPT_IGD_DATA_ID =  19 ;
NAPT_IGD_MAPPING_DATA_ID =  20 ;
NAPT_VSERVER_DATA_ID =  21 ;
LINK_DATA_ID =  22 ;
LINK_STATUS_DATA_ID =  23 ;
STATIC_IP_DATA_ID =  24 ;
DHCPC_DATA_ID =  25 ;
PPPOE_DATA_ID =  26 ;
PPPOE_LASTDIAL_DATA_ID =  27 ;
SNTPC_CONFIG_DATA_ID =  28 ;
SNTPC_TIME_DATA_ID =  29 ;
PEANUTHULL_DATA_ID =  30 ;
PEANUTHULL_STATUS_DATA_ID =  31 ;
PARENT_CTL_DATA_ID =  32 ;
BEHAVMANG_CONFIG_DATA_ID =  33 ;
WLAN_BASIC_DATA_ID =  34 ;
MBSSID_MAIN_DATA_ID =  35 ;
MBSSID_IPTV_DATA_ID =  36 ;
MBSSID_GUESTNET_DATA_ID =  37 ;
WLAN_AP_LIST_DATA_ID =  38 ;

def DataBlock():
	DEVICE = {
		id:DEVICE_DATA_ID,
		fullName:"",
		facturer:"",
		modelName:"",
		modelVer:"",
		softVer:"",
		hardVer:"",
		prodId:"",
		languId:"",
		countryId:"",
		mainVer:"",
		minorVer:"",
		oemId:""
	}

	SYSTEM ={
		id:SYSTEM_DATA_ID,
		authKey:"",
		setWzd:"",
		mode:"",
		logLevel:"",
		fastpath:"",
		mac:[]
	};

	SYSTEM_LOG ={
		id:SYSTEM_LOG_DATA_ID,
		num:"",
		list:[
		{
			level:"",
			days:"",
			hours:"",
			mins:"",
			secs:"",
			msecs:"",
			msg:""
		}]
	};

	EXCEPT_LOG ={
		id:EXCEPT_LOG_DATA_ID,
		num:"",
		list:[
		{
			msg:""
		}]
	};

	LAN ={
		id:LAN_DATA_ID,
		ip:"",
		mask:"",
		mode:""
	};

	LCLPORT ={
		id:LCLPORT_DATA_ID,
		port:""
	};

	LCLHOST ={
		id:LCLHOST_DATA_ID,
		enableAll:"",
		mac:[]
	};

	RMTHOST ={
		id:RMTHOST_DATA_ID,
		port:"",
		rule:"",
		addr:""
	};

	DHCPS ={
		id:DHCPS_DATA_ID,
		enable:"",
		poolStart:"",
		poolEnd:"",
		leaseTime:"",
		dns:[],
		gateway:"",
		hostName:""
	};

	DHCPS_LEASE ={
		id:DHCPS_LEASE_DATA_ID,
		list:[
		{
			hostName:"",
			mac:"",
			reserved:"",
			state:"",
			ip:"",
			expires:""
		}]
	};

	TPDOMAIN ={
		id:TPDOMAIN_DATA_ID,
		enable:"",
		name:""
	};

	FACTORY ={
		id:FACTORY_DATA_ID,
		lanIp:"",
		lanMask:"",
		authKey:""
	};

	STACTRLTBL ={
		id:STACTRLTBL_DATA_ID,
		list:[
		{
			ip:"",
			mac:"",
			reserved:"",
			bindEntry:"",
			staMgtEntry:"",
			name:"",
			blocked:"",
			upLimit:"",
			downLimit:""
		}]
	};

	STARTTABLE ={
		id:STARTTABLE_DATA_ID,
		list:[
		{
			ip:"",
			mac:"",
			reserved:"",
			bindEntry:"",
			staMgtEntry:"",
			type:"",
			online:"",
			blocked:"",
			up:"",
			down:"",
			upLimit:"",
			downLimit:"",
			name:""
		}]
	};

	STATIC_ROUTE ={
		id:STATIC_ROUTE_DATA_ID,
		list:[
		{
			enable:"",
			net:"",
			mask:"",
			gateway:""
		}]
	};

	DYNAMIC_ROUTE ={
		id:DYNAMIC_ROUTE_DATA_ID,
		list:[
		{
			net:"",
			mask:"",
			gateway:""
		}]
	};

	SYSTEM_ROUTE ={
		id:SYSTEM_ROUTE_DATA_ID,
		list:[
		{
			net:"",
			gateway:"",
			mask:"",
			netif:""
		}]
	};

	NAPT_ALG ={
		id:NAPT_ALG_DATA_ID,
		ftpAlgEnable:"",
		pptpAlgEnable:"",
		rtspAlgEnable:"",
		sipAlgEnable:"",
		ipsecAlgEnable:"",
		h323AlgEnable:""
	};

	NAPT_DMZ ={
		id:NAPT_DMZ_DATA_ID,
		dmzEnable:"",
		dmzClient:""
	};

	NAPT_IGD ={
		id:NAPT_IGD_DATA_ID,
		igdEnable:""
	};

	NAPT_IGD_MAPPING ={
		id:NAPT_IGD_MAPPING_DATA_ID,
		num:"",
		list:[
		{
			extPort:"",
			intPort:"",
			ptc:"",
			enabled:"",
			leaseDuration:"",
			leaseTimer:"",
			rmtHost:"",
			client:"",
			desc:""
		}]
	};

	NAPT_VSERVER ={
		id:NAPT_VSERVER_DATA_ID,
		list:[
		{
			vsEntryEnable:"",
			vsLclIp:"",
			vsRmtIp:"",
			vsLclPort:"",
			vsRmtPort:"",
			vsOpenPortS:"",
			vsOpenPortE:"",
			vsPtc:""
		}]
	};

	LINK ={
		id:LINK_DATA_ID,
		linkMode:"",
		linkType:""
	};

	LINK_STATUS ={
		id:LINK_STATUS_DATA_ID,
		ip:"",
		mask:"",
		gateway:"",
		dns:[],
		status:"",
		code:"",
		upTime:"",
		inPkts:"",
		inOctets:"",
		outPkts:"",
		outOctets:""
	};

	STATIC_IP ={
		id:STATIC_IP_DATA_ID,
		ip:"",
		mask:"",
		gateway:"",
		dns:[],
		mtu:""
	};

	DHCPC ={
		id:DHCPC_DATA_ID,
		name:"",
		dns:[],
		mtu:"",
		ucast:"",
		manualDns:""
	};

	PPPOE ={
		id:PPPOE_DATA_ID,
		svName:"",
		acName:"",
		name:"",
		paswd:"",
		fixipEnb:"",
		fixip:"",
		manualDns:"",
		dns:[],
		lcpMru:"",
		linkType:"",
		dialMode:"",
		maxIdleTime:""
	};

	PPPOE_LASTDIAL ={
		id:PPPOE_LASTDIAL_DATA_ID,
		acMac:"",
		reserved:"",
		sessionid:"",
		dialMode:"",
		ncTimes:""
	};

	SNTPC_CONFIG ={
		id:SNTPC_CONFIG_DATA_ID,
		timeZone:""
	};

	SNTPC_TIME ={
		id:SNTPC_TIME_DATA_ID,
		year:"",
		month:"",
		day:"",
		hour:"",
		minute:"",
		second:"",
		sntpcSuccess:""
	};

	PEANUTHULL ={
		id:PEANUTHULL_DATA_ID,
		autoConnect:"",
		name:"",
		password:""
	};

	PEANUTHULL_STATUS ={
		id:PEANUTHULL_STATUS_DATA_ID,
		status:"",
		type:"",
		num:"",
		domains:[]
	};

	PARENT_CTL ={
		id:PARENT_CTL_DATA_ID,
		enable:"",
		mon:"",
		tue:"",
		wed:"",
		thu:"",
		fri:"",
		sat:"",
		sun:"",
		list:[
		{
			mac:"",
			reserved:""
		}]
	};

	BEHAVMANG_CONFIG ={
		id:BEHAVMANG_CONFIG_DATA_ID,
		bhavEnable:"",
		bhavRule:"",
		rList:[
		{
			rName:"",
			rActive:"",
			rHost:"",
			rTarget:"",
			rSchedule:"",
			rReserved:""
		}],
		hList:[
		{
			hIsIp:"",
			hName:"",
			hIpStart:"",
			hIpEnd:"",
			hMac:"",
			hReserved:""
		}],
		tList:[
		{
			tType:"",
			tName:"",
			tIpStart:"",
			tIpEnd:"",
			tPortStart:"",
			tPortEnd:"",
			tProto:"",
			tUrl0:"",
			tUrl1:"",
			tUrl2:"",
			tUrl3:""
		}],
		sList:[
		{
			sName:"",
			sActive:"",
			sMon:"",
			sTue:"",
			sWed:"",
			sThu:"",
			sFri:"",
			sSat:"",
			sSun:""
		}]
	};

	WLAN_BASIC ={
		id:WLAN_BASIC_DATA_ID,
		bEnabled:"",
		uApMode:"",
		uRegionIndex:"",
		uChannel:"",
		uBgnMode:"",
		uChannelWidth:"",
		adv:
		{
			uRTSThreshold:"",
			uFragThreashold:"",
			uBeaconInterval:"",
			uPower:"",
			uDTIMInterval:"",
			bWMEEnabled:"",
			bIsolationEnabled:"",
			bShortPrmbleDisabled:"",
			bShortGI:""
		},
		apc:
		{
			bBridgeEnabled:"",
			cBridgedSsid:"",
			cBridgedBssid:"",
			uWepIndex:"",
			uSecurityType:"",
			cPassWD:"",
			uDetect:""
		},
		bTurboOn:""
	};

	MBSSID_MAIN ={
		id:MBSSID_MAIN_DATA_ID,
		uRadiusIp:"",
		uRadiusGKUpdateIntvl:"",
		uPskGKUpdateIntvl:"",
		privacyRcd:[
		{
			uKeyLength:"",
			cKeyVal:""
		}],
		uRadiusPort:"",
		uKeyType:"",
		uDefaultKey:"",
		bEnable:"",
		bBcastSsid:"",
		cSsid:"",
		bSecurityEnable:"",
		uAuthType:"",
		uWEPSecOpt:"",
		uRadiusSecOpt:"",
		uPSKSecOpt:"",
		uRadiusEncryptType:"",
		uPSKEncryptType:"",
		cRadiusSecret:"",
		cPskSecret:"",
		bSecCheck:"",
		wps:
		{
			bEnabled:"",
			cUsrPIN:"",
			bConfigured:"",
			bIsLocked:""
		}
	};

	MBSSID_IPTV ={
		id:MBSSID_IPTV_DATA_ID,
		uRadiusIp:"",
		uRadiusGKUpdateIntvl:"",
		uPskGKUpdateIntvl:"",
		privacyRcd:[
		{
			uKeyLength:"",
			cKeyVal:""
		}],
		uRadiusPort:"",
		uKeyType:"",
		uDefaultKey:"",
		bEnable:"",
		bBcastSsid:"",
		cSsid:"",
		bSecurityEnable:"",
		uAuthType:"",
		uWEPSecOpt:"",
		uRadiusSecOpt:"",
		uPSKSecOpt:"",
		uRadiusEncryptType:"",
		uPSKEncryptType:"",
		cRadiusSecret:"",
		cPskSecret:"",
		bSecCheck:"",
		wps:
		{
			bEnabled:"",
			cUsrPIN:"",
			bConfigured:"",
			bIsLocked:""
		}
	};

	MBSSID_GUESTNET ={
		id:MBSSID_GUESTNET_DATA_ID,
		uRadiusIp:"",
		uRadiusGKUpdateIntvl:"",
		uPskGKUpdateIntvl:"",
		privacyRcd:[
		{
			uKeyLength:"",
			cKeyVal:""
		}],
		uRadiusPort:"",
		uKeyType:"",
		uDefaultKey:"",
		bEnable:"",
		bBcastSsid:"",
		cSsid:"",
		bSecurityEnable:"",
		uAuthType:"",
		uWEPSecOpt:"",
		uRadiusSecOpt:"",
		uPSKSecOpt:"",
		uRadiusEncryptType:"",
		uPSKEncryptType:"",
		cRadiusSecret:"",
		cPskSecret:"",
		bSecCheck:"",
		wps:
		{
			bEnabled:"",
			cUsrPIN:"",
			bConfigured:"",
			bIsLocked:""
		},
		bLanAccess:"",
		uDuration:"",
		bSetOpenTime:"",
		uMaxUploadSpeed:"",
		uMaxDownloadSpeed:"",
		uAllowTimeMode:"",
		uTimeTable:[]
	};

	WLAN_AP_LIST ={
		id:WLAN_AP_LIST_DATA_ID,
		apEntry:[
		{
			cBssid:"",
			cSsid:"",
			uRssi:"",
			uChannel:"",
			uAuthMode:"",
			uBgnMode:"",
			uChanWidth:""
		}],
		uApCnt:""
	};