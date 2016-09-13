## -*- coding: cp936 -*-
################################ from DM.js ################################
SYN = 0;
ASYN = 1;
TDDP_INSTRUCT = 0;
TDDP_WRITE = 1;		#/* �������ݣ���Ӧ����ǰ��SET��� */
TDDP_READ = 2;		#/* ��ȡ���ݣ���Ӧ����ǰ��GET��� */
TDDP_UPLOAD = 3;	#/* ���������������TDDPV3�У�����ŵ��������У����"����������"�ֶο���ȥ���� */
TDDP_DOWNLOAD = 4;	#/* ����������á�TDDPV2������ǰ�����彫�����ǡ� */
TDDP_RESET =5;		#/* �ָ���ʼ���ã� */
TDDP_REBOOT = 6;	#/* �����豸�� */
TDDP_AUTH = 7;		#/* ��֤ */
TDDP_GETPEERMAC = 8;	#/* ��ȡ������Ϣ */
TDDP_CONFIG = 9;	#/* �����û��������� */	
TDDP_CHGPWD = 10;	#/* �޸����� */
TDDP_LOGOUT = 11;	#/* �ǳ� */

PARSE_INIT = 0;		#/* ��ʼ̬ */
PARSE_NOTE = 1;		#/* ��#��ͷ��Ϊע�͡�ע��:ֻ���ڳ�ʼ̬������#����Ϊ����ע�ͣ�����ᱻ�������ݡ� */
PARSE_CMD = 2;		#/* ������� */
PARSE_ID = 3;		#/* �������ݿ�ID�� */
PARSE_INDEX = 4;	#/* ���������� */
PARSE_VALUE = 5;	#/* ����ֵ�� */
PARSE_ERR = 6;		#/* ������������ */
					#CA1223 999-9131978274
					#CA1234 999-9131995435
					
######################### from error.js #####################################
EEXPT = -1;						#/* �쳣��� */
ENONE = 0;						#/* û�д��� */
ENOMEMORY = 1;					#/* �ڴ治�� */
EINVARG = 2;					#/* �������� */
EINVFMT = 3;					#/* ��ʽ���� */
EINVEVT = 4;					#/* ��֧�ֵ��¼� */
EINVCODE = 5;				   #
EFORBID = 6;					#/* ��ֹ�Ĳ����� */
EUNAUTH = 7;					#/* ��֤ʧ�ܡ� */
EOVERFLOW = 8;				  #
EINVINSTRUCT = 9;				#/* ��֧�ֵ�ָ�� */
EMD5 = 10;						#/* MD5У��ʧ�� */
EDESENCODE = 11;				#/* DES����ʧ�� */
EDESDECODE = 12;				#/* DES����ʧ�� */
ECHIPID = 13;					#/* ��֧�ֵ�оƬ���ͣ� */
EFLASHID = 14;					#/* ��֧�ֵ�FLASH���ͣ� */
EPRODID = 15;					#/* ��֧�ֵĲ�Ʒ�ͺţ� */
ELANGID = 16;					#/* ��֧�ֵ����ԣ� */
ESUBVER = 17;					#/* ��֧���Ӱ汾�ţ� */
EOEMID = 18;					#/* ��֧�ֵ�OEM���ͣ� */
ECOUNTRYID = 19;				#/* ��֧�ֵĹ��ң� */
ECODE = 20;						#/* ��֧�ֵĲ������ͣ� */
EWANTYPE = 21;					#/* ��֧�ֵ�WAN�ڽ������ͣ� */
ETOOLONG = 22;					#/* ���ݹ����� */
ESYSTEM = 23;					#/* ϵͳ���� */
ENOECHO = 24;					#/* ��ʱ����Ӧ�� */
ENODEVICE = 25;					#/* �Ҳ����豸�� */
EINVIP = 26;					#/* IP��ַ����ȷ�� */
EINVMASK = 27;					#/* ���벻��ȷ�� */
EINVGTW = 28;					#/* ���ز���ȷ�� */
EINVIPMASKPAIR = 29;			#/* IP�����벻ƥ�䡣 */
EGTWUNREACH = 30;				#/* ���ز��ɴ */
EINVMTU = 31;					#/* MTU���� */
EINVMACFMT = 32;				#/* MAC��ַ��ʽ����ȷ�� */
EENTRYEXIST = 33;				#/* ��Ŀ�Ѵ��ڡ� */
EENTRYNOTEXIST = 34;			#/* ��Ŀ�����ڡ� */
EENTRYCONFLIC = 35;				#/* ��Ŀ��ͻ�� */
ETABLEFULL = 36;				#/* ������ */
ETABLEEMPTY = 37;				#/* �ձ� */
EINVPORT = 38;					#/* �����˿ڷ�Χ*/
EPORTRESERVED = 39;				#/* �˿ڳ�ͻ*/
EINVPTC = 40;					#/* ��֧�ֵ�Э�����͡� */
ECOMFLICTNET = 41;				#/* ���γ�ͻ*/
EINVNET = 42;					#/* �Ƿ������� */
EINVTYPE = 43;					#/* �Ƿ������͡� */
EINVMODE = 44;					#/* �Ƿ���ģʽ�� */
EINVTIME = 45;				  #
EINVFDNSVR = 46;				#/* �Ƿ�����ѡDNS */
EINVSDNSVR = 47;				#/* �Ƿ��ı�ѡDNS */
EINVDATA = 48;					#/* ���ݺϷ�����֤ʧ�� */
EINVLEASETIME = 49;				#/* �Ƿ��ĵ�ַ���ڡ� */
EINVADDRPOOL = 50;				#/* �Ƿ��ĵ�ַ�ء� */
EINVDATE = 51;					#/* ����������� */
EINVTIMEZONE = 52;				#/* ʱ��������� */
ENOLINK = 53; 					#/*WAN��δ���� */
ESYSBUSY = 54;					#/* ϵͳ��æ�� */
EINVNUM = 55;				   #
EINVSIZE = 56;				  #
EINVTIMEOUT = 57;			   #
EINVMETRIC = 58;				#
EINVINTERVAL = 59;				#/* ʱ����������� */
EINVBOOL = 69;					#/* �������͵�ȡֵֻ����0����1 */
EINVSSIDLEN = 70;				#/* ����SSID���Ȳ��Ϸ� */
EINVSECAUTH = 71;				#/* ���߰�ȫ���õ���֤���ʹ��� */
EINVWEPAUTH = 72;				#/* WEP��֤���ʹ��� */
EINVRADIUSAUTH = 73;			#/* RADIUS��֤���ʹ��� */
EINVPSKAUTH = 74;				#/* PSK��֤���ʹ��� */
EINVCIPHER = 75;				#/* �����㷨���� */
EINVRADIUSLEN = 76;				#/* radius��Կ���ﳤ�ȴ��� */
EINVPSKLEN = 77;				#/* psk��Կ������� */
EINVGKUPINTVAL = 78;			#/* ����Կ�������ڴ��� */
EINVWEPKEYTYPE = 79;			#/* WEP��Կ���ʹ��� */
EINVWEPKEYIDX = 80;				#/* Ĭ��WEP��Կ�������� */
EINVWEPKEYLEN = 81;				#/* WEP��Կ���ȴ��� */
EINVACLDESCLEN = 82;			#/* MAC��ַ������Ŀ������Ϣ���ȴ��� */
EINVWPSPINLEN = 83;				#/* WPS PIN�볤�ȴ��� */
EINVAPMODE = 84;				#/* �����豸����ģʽ���� */
EINVWLSMODE = 85;				#/* ��������ģʽ(bgn)���� */
EINVREGIONIDX = 86;				#/* ���߹�������� */
EINVCHANWIDTH = 87;				#/* Ƶ�δ������ */
EINVRTSTHRSHLD = 88;			#/* ����RTS��ֵ���� */
EINVFRAGTHRSHLD = 89;			#/* ���߷�Ƭ��ֵ���� */
EINVBCNINTVL = 90;				#/* ����beacon������� */
EINVTXPWR = 91;					#/* ����Tx���ʴ��� */
EINVDTIMINTVL = 92;				#/* ����DTIM���ڴ��� */	
EINVWDSAUTH = 93;				#/* ����WDS��֤���ʹ��� */
EINVA34DETECT = 94;				#/* 3/4��ַ��ʽ���ô��� */
EINVWLANPWD = 95;				#/* invalid pwd */
EINVHOSTNAMELEN = 96;			#/* hostname is null */
EINVSPEEDCFG = 97;				#/* guestNet ����ϴ��ٶȻ���������ٶ����ô��� */
EINVTIMEOUTCFG = 98;			#/* guestNet ��ʱ���ô��� */
EINVMACGROUP = 99;				#/* MAC��ַΪ�鲥��ַ */
ENAMEBLANK = 100;				#/* �û�������Ϊ�� */
EPWDBLANK = 101;				#/* ��������Ϊ�� */
EINVMACZERO = 102;				#/* MAC��ַȫ�� */
EINVMACBROAD = 103;				#/* �㲥��ַ��MAC��ַ */
EHOSTNAMEEMP = 104;				#/* �ܿ�������Ϊ�� */
EOBJNAMEEMP = 105;				#/* ����Ŀ����Ϊ�� */
EPLANNAMEEMP = 106;				#/* �ճ̼ƻ���Ϊ�� */
EOBJDOMAINALLEMP = 107;			#/* ����Ŀ������ȫΪ�� */
EREFERED = 108;					#/* ��Ŀ�������� */
EDELPARTIAL = 109;				#/* ֻɾ���˲�����Ŀ */
EDELNOTHING = 110;				#/* һ����Ŀ��û��ɾ�� */
ERSACHECK = 111;				#/* RSAУ����� */
EINVLGPWDLEN = 112;				#/* ��¼���볤�Ȳ��Ϸ� */
EINLGVALCHAR = 113;				#/* ��¼���뺬�зǷ��ַ� */
EINLGVALOLDSAME = 114;			#/* �µ�¼����;ɵ�¼����һ�� */
EINVNETID = 115;				#/* �����ȫ0����1 */
EINVHOSTID = 116;				#/* ������ȫ0����1 */
EOUTOFRANGE = 117;				#/* ������Χ */
EINDOMAIN = 118;				#/* �Ƿ������� */
ELACKCFGINFO = 119;				#/* ȱ�ٱ�Ҫ��������Ϣ */
EINVKEY = 120;					#/* ��������� */
EINVRMTPORT = 121;				#/* Զ�̹���˿ڳ�����Χ*/
EILLEGALPORT = 122;				#/* �˿�ֵ�Ƿ� */
EINVNAMELEN = 123;				#/* �û������ȳ�����Χ */
EINVPWDLEN = 124;				#/* ���볤�ȳ�����Χ */
EINVNAME = 125;					#/* �û����Ƿ� */
ENOTLANSUBNET = 126;			#/* ����LAN����IP */
EHOSTALLEMPTY = 127;			#/* �ܿ�����IPȫΪ�� */
EOBJALLEMPTY = 128;				#/* ����Ŀ��IP�Ͷ˿�ȫΪ�� */
EINVGROUPIP = 129;				#/* �鲥��IP��ַ */
EINVLOOPIP = 130;				#/* �ػ���IP��ַ */
EINVIPFMT = 131;				#/* IP��ַ��ʽ���� */
ENOTLANWANNET = 132;			#/* ���β���LAN��WAN */
ELANSUBNET = 133;				#/* LAN����IP */
EINVPWD = 134;					#/* ����Ƿ� */
EIPRESERVED = 135;				#/* IP��ַ��ռ�� */
EINVPORTFMT = 136;				#/* �˿ڸ�ʽ���� */

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