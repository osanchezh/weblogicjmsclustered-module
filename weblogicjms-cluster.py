# @author: Sanchez Huerta Octavio
# @email: osanchezhuerta@gmail.com
# @homepage: https://zeosaho.blogspot.com

import sys
from java.io import FileInputStream
from java.util import Properties

def loadProperties(fileName):
	properties = Properties()
	input = FileInputStream(fileName)
	properties.load(input)
	input.close()
	result= {}
	for entry in properties.entrySet(): result[entry.key] = entry.value
	return result

ruta_propiedades=sys.argv[1]
if not ruta_propiedades:
  			print 'Configuration file was not found at the args parameters.'
else:
     print 'File to load: '+ruta_propiedades

properties = loadProperties(ruta_propiedades)


environment = properties['environment']

adminusername = properties['adminusername']
adminpassword = properties['adminpassword']
adminserverurl = properties['adminserverurl']

machineName = properties['machineName']
clusterName = properties['clusterName']
serverName1 = properties['serverName1']
serverName2 = properties['serverName2']
serverName3 = properties['serverName3']
serverName4 = properties['serverName4']
serverName5 = properties['serverName5']


serverListenPort1 = properties['serverListenPort1']
serverListenPort2 = properties['serverListenPort2']
serverListenPort3 = properties['serverListenPort3']
serverListenPort4 = properties['serverListenPort4']
serverListenPort5 = properties['serverListenPort5']


serverListenAddress1 = properties['serverListenAddress1']
serverListenAddress2 = properties['serverListenAddress2']
serverListenAddress3 = properties['serverListenAddress3']
serverListenAddress4 = properties['serverListenAddress4']
serverListenAddress5 = properties['serverListenAddress5']


jvmdirectory = properties['jvmdirectory']
javaVendor = properties['javaVendor']
javaArguments = properties['javaArguments']


moduleName = properties['moduleName']
subDeploymentName = properties['subDeploymentName']
fileStoreName1 = properties['fileStoreName1']
fileStoreName2 = properties['fileStoreName2']
fileStoreName3 = properties['fileStoreName3']
fileStoreName4 = properties['fileStoreName4']
fileStoreName5 = properties['fileStoreName5']


jmsServerName1 = properties['jmsServerName1']
jmsServerName2 = properties['jmsServerName2']
jmsServerName3 = properties['jmsServerName3']
jmsServerName4 = properties['jmsServerName4']
jmsServerName5 = properties['jmsServerName5']


fileStoreDirectory1 = properties['fileStoreDirectory1']
fileStoreDirectory2 = properties['fileStoreDirectory2']
fileStoreDirectory3 = properties['fileStoreDirectory3']
fileStoreDirectory4 = properties['fileStoreDirectory4']
fileStoreDirectory5 = properties['fileStoreDirectory5']



dsName=properties["datasource.name"]
dsDatabaseName=properties["datasource.database.name"]
datasourceTarget=properties["datasource.target"]
dsJNDIName=properties["datasource.jndiname"]
dsDriverName=properties["datasource.driver.class"]
dsURL=properties["datasource.url"]
dsUserName=properties["datasource.username"]
dsPassword=properties["datasource.password"]
dsTestQuery=properties["datasource.test.query"]


print 'CONNECT TO ADMIN SERVER'
connect(adminusername, adminpassword, adminserverurl)
adminServerName = cmo.adminServerName

try:

	print "**WEBLOGIC 11G **"
	domainName = cmo.name
	cd("Servers/%s" % adminServerName)
	adminServer = cmo

	# Delete old resources, if they exist.
	def deleteIgnoringExceptions(mbean):
		try: delete(mbean)
		except: 
			print "delete mbean"
			pass
	
	def startTransaction():
		edit()
		startEdit()

	def endTransaction():
		save()
		activate(block="true")

	def createCluster():
		print "createCluster() START"

		print 'CREATE MACHINE: machine1';
		machine1 = cmo.createUnixMachine(machineName);
		machine1.setPostBindUIDEnabled(false);
		#machine1.setPostBindUID('root');
		machine1.getNodeManager().setListenAddress('127.0.0.1');
		machine1.getNodeManager().setNMType('ssl');

		print 'CREATE CLUSTER: CLUSTER';
                print 'clusterName:'+clusterName
		cluster = cmo.createCluster(clusterName);
		cluster.setClusterMessagingMode('unicast');

		print 'CREATE MANAGED SERVER: server1';
                print serverName1
		print serverListenPort1
		print serverListenAddress1
		print jvmdirectory
		print javaVendor
		print javaArguments
                print '...inicia ' + cmo.name
		server1 = cmo.createServer(serverName1);
		print '...cmo.createServer'
		server1.setListenPort(int(serverListenPort1));
		server1.setListenAddress(serverListenAddress1);
		print '...server1.setListenAddress'
		server1.setAutoRestart(true);
		server1.setAutoKillIfFailed(true);
		server1.setRestartMax(2);
		server1.setRestartDelaySeconds(10);
		server1.getServerStart().setJavaHome(jvmdirectory);
		server1.getServerStart().setJavaVendor(javaVendor);
		server1.getServerStart().setArguments(javaArguments);
		print '...fin'

		print 'CREATE MANAGED SERVER: server2';
		server2 = cmo.createServer(serverName2);
		server2.setListenPort(int(serverListenPort2));
		server2.setListenAddress(serverListenAddress2);
		server2.setAutoRestart(true);
		server2.setAutoKillIfFailed(true);
		server2.setRestartMax(2);
		server2.setRestartDelaySeconds(10);
		server2.getServerStart().setJavaHome(jvmdirectory);
		server2.getServerStart().setJavaVendor(javaVendor);
		server2.getServerStart().setArguments(javaArguments);

		print 'ADD MANAGED SERVERS TO CLUSTER';
		server1.setCluster(cluster);
		server2.setCluster(cluster);

		print 'ADD MANAGED SERVERS TO MACHINE';
		server1.setMachine(machine1);
		server2.setMachine(machine1);


		print "createCluster() END"

        def createDataSource():
 		print "createDataSource() START"

		cd('/')
		cmo.createJDBCSystemResource(dsName)
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
		cmo.setName(dsName)
                print "createDataSource() START 1"
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
		set('JNDINames',jarray.array([String('jdbc/' + dsName )], String))
                print "createDataSource() START 2"
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
		cmo.setUrl(dsURL)
		cmo.setDriverName( dsDriverName )
		cmo.setPassword(dsPassword)
                print "createDataSource() START 3"
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
		cmo.setTestTableName(dsTestQuery)
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
		cmo.createProperty('user')
                
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
		cmo.setValue(dsUserName)
                
                print "createDataSource() START 4"
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
		cmo.createProperty('databaseName')

		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/databaseName')
		cmo.setValue(dsDatabaseName)
                
                print "createDataSource() START 5"
		cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
		cmo.setGlobalTransactionsProtocol('OnePhaseCommit')
                
                print "createDataSource() START 6:"+datasourceTarget
		cd('/SystemResources/' + dsName )
		set('Targets',jarray.array([ObjectName('com.bea:Name=' + datasourceTarget + ',Type=Server')], ObjectName))
                
                print "createDataSource() START 7"
                
		print "createDataSource() END"

	def createDLQ(qname, qjndiname,dkName):
		print "createDLQ() START"
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)
		errorQueue = create(qname, "Queue")
		errorQueue.JNDIName = qjndiname

		# Set JMS Subdeployment		
		errorQueue.subDeploymentName = subDeploymentName
                print dkName

		#errorQueue.setDestinationKeys = dkName
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)                		
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname)
		set('DestinationKeys',jarray.array([String(dkName)],String))
		# Set redeliver limit and do LOG when max redeliver times occured
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/DeliveryFailureParams/'+qname)
		cmo.setRedeliveryLimit(1)
		cmo.setExpirationPolicy('Log')
		
		# Set delay (miliseconds) on redeliver
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setRedeliveryDelay(5000)

		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/DeliveryFailureParams/'+qname)
		cmo.unSet('ErrorDestination')

		# Set Persistenr Delivery Mode
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setPriority(-1)
		cmo.setDeliveryMode('Persistent')
		cmo.setTimeToDeliver('-1')
		cmo.setTimeToLive(-1)
		print "createDLQ() END"
	
	def createDestinationKey(dkname):
        	print "createDestinationKey() START"     
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)
		dk1 = create(dkname, "DestinationKey")
		#cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/DestinationKeys/'+dkName)
                dk1.setProperty("JMSPriority")
		dk1.setKeyType("String")
		dk1.setSortOrder("Descending")
        	print "createDestinationKey() END"

	def createQueue(qname, qjndiname, dlqName,dkName):
		print "createQueue() START"
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)
		q1 = create(qname, "Queue")
		q1.JNDIName = qjndiname


		q1.subDeploymentName = subDeploymentName
		#errorQueue.setDestinationKeys = dkName
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)                		
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname)
		set('DestinationKeys',jarray.array([String(dkName)],String))

		# Set delay (miliseconds) on redeliver
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setRedeliveryDelay(2000)

		print "Assign failed destination to queue"
		# Set redeliver limit
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/DeliveryFailureParams/'+qname)
		cmo.setRedeliveryLimit(3)
		# Set Failed Destination Delivery to another queue
		cmo.setExpirationPolicy('Redirect')
		erQueue = getMBean('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+dlqName)
		cmo.setErrorDestination(erQueue)

		# Enable Logging for Queue
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/MessageLoggingParams/'+qname)
		cmo.setMessageLoggingEnabled(true)
		cmo.setMessageLoggingFormat('JMSDestination,JMSMessageID')

		# Set Persistenr Delivery Mode
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setPriority(-1)
		cmo.setDeliveryMode('Persistent')
		cmo.setTimeToDeliver('-1')
		cmo.setTimeToLive(-1)
		print "createQueue() END"

	def createUniformDistributedDLQ(qname, qjndiname,dkName):
		print "createUniformDistributedDLQ() START"
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)
		errorQueue = create(qname, "UniformDistributedQueue")
		errorQueue.JNDIName = qjndiname

		# Set JMS Subdeployment		
		errorQueue.subDeploymentName = subDeploymentName
                print dkName

		#errorQueue.setDestinationKeys = dkName
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)                		
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname)
		set('DestinationKeys',jarray.array([String(dkName)],String))
		# Set redeliver limit and do LOG when max redeliver times occured
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/DeliveryFailureParams/'+qname)
		cmo.setRedeliveryLimit(1)
		cmo.setExpirationPolicy('Log')
		
		# Set delay (miliseconds) on redeliver
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setRedeliveryDelay(5000)

		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/DeliveryFailureParams/'+qname)
		cmo.unSet('ErrorDestination')

		# Set Persistenr Delivery Mode
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setPriority(-1)
		cmo.setDeliveryMode('Persistent')
		cmo.setTimeToDeliver('-1')
		cmo.setTimeToLive(-1)
		print "createUniformDistributedDLQ() END"

	def createUniformDistributedQueue(qname, qjndiname, dlqName,dkName):
		print "createUniformDistributedQueue() START"
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)
		udq1 = create(qname, "UniformDistributedQueue")
		#cmo.createUniformDistributedQueue('DistributedQueue-0')
		print 'udq1.JNDIName = qjndiname'
		udq1.JNDIName = qjndiname
		udq1.subDeploymentName = subDeploymentName

		# Set JMS Subdeployment		
		#udq1.subDeploymentName = subDeploymentName
		print 'udq1.destinationKey= dkName'
		#errorQueue.setDestinationKeys = dkName
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)   
		print 'udq1.destinationKey= dkName 1'             		
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname)
		print 'udq1.destinationKey= dkName 2'		
		set('DestinationKeys',jarray.array([String(dkName)],String))
		
		print 'udq1.setLoadBalancingPolicy= dkName 1'
		#resource = module.getJMSResource();
		print 'udq1.setLoadBalancingPolicy= dkName 2'
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname)
		cmo.setLoadBalancingPolicy('Round-Robin')

		#distributedqueue = resource.lookupUniformDistributedQueue(qname);
		#distributedqueue.setJNDIName('jms/CompanyQueue');
		#print 'udq1.setLoadBalancingPolicy= dkName'
		#distributedqueue.setLoadBalancingPolicy('Round-Robin');
		#print 'udq1.setSubDeploymentName= dkName'
		#distributedqueue.setSubDeploymentName(subDeploymentName);

                #udq1.loadBalancingPolicy='Round-Robin'
		print 'Set delay (miliseconds) on redeliver'
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setRedeliveryDelay(2000)

		print "Assign failed destination to queue"
		print 'Set redeliver limit'
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/DeliveryFailureParams/'+qname)
		cmo.setRedeliveryLimit(3)
		print 'Set Failed Destination Delivery to another queue'
		cmo.setExpirationPolicy('Redirect')
		erQueue = getMBean('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+dlqName)
		cmo.setErrorDestination(erQueue)

		print 'Enable Logging for Queue'
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/MessageLoggingParams/'+qname)
		cmo.setMessageLoggingEnabled(true)
		cmo.setMessageLoggingFormat('JMSDestination,JMSMessageID')

		print 'Set Persistent Delivery Mode'
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/UniformDistributedQueues/'+qname+'/DeliveryParamsOverrides/'+qname)
		cmo.setPriority(-1)
		cmo.setDeliveryMode('Persistent')
		cmo.setTimeToDeliver('-1')
		cmo.setTimeToLive(-1)
		print "createUniformDistributedQueue() END"

	def createCF(cfname, cfjndiname, xaEnabled):
		print "createCF() START"
		cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)
		cf = create(cfname, "ConnectionFactory")
		cf.JNDIName = cfjndiname
		cf.subDeploymentName = subDeploymentName
		# Set XA transactions enabled
		if (xaEnabled == "true"):
			cf.transactionParams.setXAConnectionFactoryEnabled(1)
		print "createCF() END"


	def createJMSModule(cjmsserver1,cjmsserver2,cjmsserver3,cjmsserver4,cjmsserver5):
		print "createJMSModule() START"
		cd('/JMSSystemResources')
		jmsModule = create(moduleName, "JMSSystemResource")
		cd('/')
		clusternm = getMBean('/Clusters/' + clusterName)
		jmsModule.targets = (clusternm,)	
	
		#cd(jmsModule.name)
		# Create and configure JMS Subdeployment for this JMS System Module		
		#sd = create(subDeploymentName, "SubDeployment")	
		#myJMSServer = getMBean('/JMSServers/' + jmsServerName)
		#sd.targets = (myJMSServer,)
		#print "createJMSModule() END"
		cd('/JMSSystemResources')
                cd(jmsModule.name)
		print 'CREATE SUBDEPLOYMENT';
		#sd.createSubDeployment(subDeploymentName);
		print 'subDeploymentName: '+subDeploymentName
		sd = create(subDeploymentName, "SubDeployment")
   		print 'subDeploymentName: '+subDeploymentName + "... raiz"
		cd('/JMSSystemResources/'+moduleName+'/SubDeployments/'+subDeploymentName);
		print 'subDeploymentName: '+subDeploymentName + "... raiz 1"
		set('Targets',jarray.array([ObjectName('com.bea:Name='+cjmsserver1+',Type=JMSServer'), 
                ObjectName('com.bea:Name='+cjmsserver2+',Type=JMSServer'), 
                ObjectName('com.bea:Name='+cjmsserver3+',Type=JMSServer'), 
                ObjectName('com.bea:Name='+cjmsserver4+',Type=JMSServer'), 
                ObjectName('com.bea:Name='+cjmsserver5+',Type=JMSServer')], ObjectName));
		print 'subDeploymentName: '+subDeploymentName + "... raiz 2"
		cd('/');
		print "createJMSModule() END"
		#errorQueue.setDestinationKeys = dkName
		#cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName)                		
		#cd('/JMSSystemResources/'+moduleName+'/JMSResource/'+moduleName+'/Queues/'+qname)
		#set('DestinationKeys',jarray.array([String(dkName)],String))


	def createJMSServer(cjmsserver,cfilestore,cfilestoredirectory, pservername):
		print "createJMSServer() START"
		startTransaction()
		# Delete existing JMS Server and its Filestore
		cd("/JMSServers")
		deleteIgnoringExceptions(cjmsserver)
		cd("/FileStores")
		deleteIgnoringExceptions(cfilestore)

		# Create Filestore
		cd('/')
		filestore = cmo.createFileStore(cfilestore)
		filestore.setDirectory(cfilestoredirectory)
                print 'ini obtener cluster'
		servernm = getMBean('/Servers/' + pservername)
		print 'pservername='+pservername
		print 'fin obtener cluster'
		filestore.targets = (servernm,)
		print 'inicio endTransaction tar obtener cluster'
		endTransaction()
		print 'fin endTransaction tar obtener cluster'
		startTransaction()
		cd("/JMSServers")
		# Create JMS server and assign the Filestore
		jmsServer = create(cjmsserver, "JMSServer")
		jmsServer.setPersistentStore(filestore)


	startTransaction()
	print 'Delete existing JMS Module'
	cd("/JMSSystemResources")
	deleteIgnoringExceptions(moduleName)
	endTransaction()

	print "DEGIN Create JMS Server 1"
	createJMSServer(jmsServerName1,fileStoreName1,fileStoreDirectory1,serverName1)
	print "END Create JMS Server 1"
	print "Create JMS Server 2"
	createJMSServer(jmsServerName2,fileStoreName2,fileStoreDirectory2,serverName2)
	print "END Create JMS Server 2"
	print "Create JMS Server 3"
	createJMSServer(jmsServerName3,fileStoreName3,fileStoreDirectory3,serverName3)
	print "END Create JMS Server 3"
	print "Create JMS Server 4"
	createJMSServer(jmsServerName4,fileStoreName4,fileStoreDirectory4,serverName4)
	print "END Create JMS Server 4"
	print "Create JMS Server 5"
	createJMSServer(jmsServerName5,fileStoreName5,fileStoreDirectory5,serverName5)
	print "END Create JMS Server 5"


	startTransaction()
	print "Create JMS Module BEGIN"
	createJMSModule(jmsServerName1,jmsServerName2,jmsServerName3,jmsServerName4,
        jmsServerName5)
	print "Create JMS Module END"
        
	# Create an Error Destination Queue to redirect messages to this queue,
	# when the message(s) has reached the maximum redelivered times.

	#DestinationKey
	dkName1='DefaultDestinationKey'
	print "Create Destination Key DefaultDestinationKey"
	createDestinationKey(dkName1)

	#ApplicationBatch

	queueEDQName1 = 'ApplicationBatchErrorQueue'
	queueEDQJNDIName1 = 'jms/ApplicationBatchErrorQueue'
	print "Create Error Destinantion ApplicationBatchErrorQueue"
	createUniformDistributedDLQ(queueEDQName1, queueEDQJNDIName1,dkName1)
	
	queueName1 = 'ApplicationBatchReplyQueue'
	queueJNDIName1 = 'jms/ApplicationBatchReplyQueue'
	print "Create Queue ApplicationBatchReplyQueue"
	createUniformDistributedQueue(queueName1, queueJNDIName1, queueEDQName1,dkName1)
	
	queueName2 = 'ApplicationBatchRequestQueue'
	queueJNDIName2 = 'jms/ApplicationBatchRequestQueue'
	print "Create Queue ApplicationBatchRequestQueue"
	createUniformDistributedQueue(queueName2, queueJNDIName2, queueEDQName1,dkName1)
	
	#EnvioDeclaracionesyPagos

	queueEDQName2 = 'EnvioDeclaracionesyPagosErrorQueue'
	queueEDQJNDIName2 = 'jms/EnvioDeclaracionesyPagosErrorQueue'
	print "Create Error Destinantion EnvioDeclaracionesyPagosErrorQueue"
	createUniformDistributedDLQ(queueEDQName2, queueEDQJNDIName2,dkName1)
	
	queueName3 = 'EnvioDeclaracionesyPagosReplyQueue'
	queueJNDIName3 = 'jms/EnvioDeclaracionesyPagosReplyQueue'
	print "Create Queue EnvioDeclaracionesyPagosReplyQueue"
	#createQueue(queueName3, queueJNDIName3, queueEDQName2,dkName1)
	createUniformDistributedQueue(queueName3, queueJNDIName3, queueEDQName2,dkName1)

	queueName4 = 'EnvioDeclaracionesyPagosRequestQueue'
	queueJNDIName4 = 'jms/EnvioDeclaracionesyPagosRequestQueue'
	print "Create Queue EnvioDeclaracionesyPagosRequestQueue"
	#createQueue(queueName4, queueJNDIName4, queueEDQName2,dkName1)
	createUniformDistributedQueue(queueName4, queueJNDIName4, queueEDQName2,dkName1)

	#XMLMarshaller

	queueEDQName3 = 'XMLMarshallerErrorQueue'
	queueEDQJNDIName3 = 'jms/XMLMarshallerErrorQueue'
	print "Create Error Destinantion XMLMarshallerErrorQueue"
	createUniformDistributedDLQ(queueEDQName3, queueEDQJNDIName3,dkName1)
	
	queueName5 = 'XMLMarshallerReplyQueue'
	queueJNDIName5 = 'jms/XMLMarshallerReplyQueue'
	print "Create Queue XMLMarshallerReplyQueue"
	#createQueue(queueName5, queueJNDIName5, queueEDQName3,dkName1)
	createUniformDistributedQueue(queueName5, queueJNDIName5, queueEDQName3,dkName1)

	queueName6 = 'XMLMarshallerRequestQueue'
	queueJNDIName6 = 'jms/XMLMarshallerRequestQueue'
	print "Create Queue XMLMarshallerRequestQueue"
	#createQueue(queueName6, queueJNDIName6, queueEDQName3,dkName1)
	createUniformDistributedQueue(queueName6, queueJNDIName6, queueEDQName3,dkName1)

	myCFName = 'DyPConnectionFactory'
	myCFJNDIName = 'jms/DyPConnectionFactory'
	print "Create JMS XA Connection Factory DyPConnectionFactory"
	createCF(myCFName, myCFJNDIName, "true")
	
	
	endTransaction()

except:
	print "ERROR ON THE EXECUTION:"
	dumpStack()
	cancelEdit("y")
	#raise

print "disconnect"
disconnect()

print "exit"
exit();
