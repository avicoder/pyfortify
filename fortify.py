from .base import Fortify

class Connect(Fortify):

	BASE_PATH = ''
	URLS = {
		'activityFeedEvents':'/activityFeedEvents',
		'alertDefinitions':'/alertDefinitions',
		'alertableEventTypes':'/alertableEventTypes',
		'alerts':'/alerts',
		'attributeDefinitions':'/attributeDefinitions',
		'authEntities':'/authEntities',
		'bugfieldTemplateGroups':'/bugfieldTemplateGroups',
		'bugtrackers':'/bugtrackers',
		'bulk':'/bulk',
		'cloudjobs':'/cloudjobs',
		'cloudpools':'/cloudpools',
		'cloudsystem':'/cloudsystem',
		'cloudworkers':'/cloudworkers',
		'coreRulepacks':'/coreRulepacks',
		'customTags':'/customTags',
		'engineTypes':'/engineTypes',
		'events':'/events',
		'fileTokes':'/fileTokes',
		'folders':'/folders',
		'issueDetails':'/issueDetails',
		'issueTemplates':'/issueTemplates',
		'issueaging':'/issueaging',
		'issueaginggroup':'/issueaginggroup',
		'issues':'/issues',
		'jobs':'/jobs',
		'ldapObjects':'/ldapObjects',
		'localUsers':'/localUsers',
		'performanceIndicators':'/performanceIndicators',
		'permissions':'/permissions',
		'personas':'/personas',
		'portlets':'/portlets',
		'projectVersions':'/projectVersions',
		'projects':'/projects',
		'reportDefinitions':'/reportDefinitions',
		'reportLibraries':'/reportLibraries',
		'reports':'/reports',
		'roles':'/roles',
		'scans':'/scans',
		'updateRulepacks':'/updateRulepacks',
		'userSession':'/userSession',
		'validateSearchString':'/validateSearchString',
		'variables':'/variables'
	}

	def __init__(self):
		super(Connect,self).__init__()

	def alerts(self,**kwargs):
		path = self._get_id_path('alerts')
		response = self._GET(path,kwargs)
		return response


	def alertableEventTypes(self,**kwargs):
		path = self._get_id_path('alertableEventTypes')
		response = self._GET(path,kwargs)
		return response

	def alertDefinitions(self, id=None,  **kwargs):
		path =  self._get_id_path('alertDefinitions')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def activityFeedEvents(self,**kwargs):
		path = self._get_id_path('activityFeedEvents')
		response = self._GET(path,kwargs)
		return response


	def attributeDefinitions(self,id=None,**kwargs):
		path = self._get_id_path('attributeDefinitions')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response


	def authEntities(self,id=None,**kwargs):
		path = self._get_id_path('authEntities')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def authEntitiesGroups(self,parent_id,**kwargs):
		path = self._get_id_path('authEntities')
		path = '{0}/{1}/groups'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def authEntitiesProjectVersions(self,parent_id,**kwargs):	
		path = self._get_id_path('authEntities')
		path = '{0}/{1}/projectVersions'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def authEntitiesRoles(self,parent_id,**kwargs):	
		path = self._get_id_path('authEntities')
		path = '{0}/{1}/roles'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response
	

	def bugfieldTemplateGroups(self,id=None,**kwargs):
		path = self._get_id_path('bugfieldTemplateGroups')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response


	def bugtrackers(self,**kwargs):
		path = self._get_id_path('bugtrackers')
		response = self._GET(path,kwargs)
		return response


	def bulk(self,**kwargs):
		path = self._get_id_path('bulk')
		response = self._GET(path,kwargs)
		return response


	def bugfieldTemplateGroups(self,id=None,**kwargs):
		path = self._get_id_path('bugfieldTemplateGroups')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def cloudjobs(self,id=None,**kwargs):
		path = self._get_id_path('cloudjobs')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response


	def cloudPools(self,id=None,**kwargs):
		path = self._get_id_path('cloudpools')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def cloudPoolsDisabledWorkers(self,id=None,**kwargs):
		path = self._get_id_path('cloudpools')
		path = '{0}/{1}'.format(path,'disabledWorkers')
		response = self._GET(path,kwargs)
		return response


	def cloudpoolsJobs(self,parent_id,**kwargs):
		path = self._get_id_path('cloudpools')
		path = '{0}/{1}/jobs'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def cloudpoolsVersions(self,parent_id,**kwargs):
		path = self._get_id_path('cloudpools')
		path = '{0}/{1}/versions'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def cloudpoolsVersionsAction(self,parent_id,**kwargs):
		path = self._get_id_path('cloudpools')
		path = '{0}/{1}/versions/action'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def cloudpoolsWorkers(self,parent_id,**kwargs):
		path = self._get_id_path('cloudpools')
		path = '{0}/{1}/workers'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def cloudpoolsWorkersAction(self,parent_id,**kwargs):
		path = self._get_id_path('cloudpools')
		path = '{0}/{1}/workers/action'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def cloudsystemMetrics(self,**kwargs):
		path = self._get_id_path('cloudsystem')
		path = '{0}/{1}'.format(path,'metrics')
		response = self._GET(path,kwargs)
		return response


	def cloudsystemPollstatus(self,**kwargs):
		path = self._get_id_path('cloudsystem')
		path = '{0}/{1}'.format(path,'pollstatus')
		response = self._GET(path,kwargs)
		return response


	def cloudsystemsettings(self,**kwargs):
		path = self._get_id_path('cloudsystem')
		path = '{0}/{1}'.format(path,'settings')
		response = self._GET(path,kwargs)
		return response

	def cloudworkers(self,id=None,**kwargs):
		path = self._get_id_path('cloudworkers')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def cloudworkersCloudjobs(self,parent_id,**kwargs):
		path = self._get_id_path('cloudworkers')
		path = '{0}/{1}/cloudjobs'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def coreRulepacks(self,id=None,**kwargs):
		path = self._get_id_path('coreRulepacks')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def customTags(self,id=None,**kwargs):
		path = self._get_id_path('customTags')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def engineTypes(self,**kwargs):
		path = self._get_id_path('engineTypes')
		response = self._GET(path,kwargs)
		return response

	def events(self,**kwargs):
		path = self._get_id_path('events')
		response = self._GET(path,kwargs)
		return response

	def fileTokes(self,**kwargs):
		path = self._get_id_path('fileTokes')
		response = self._GET(path,kwargs)
		return response

	def folders(self,**kwargs):
		path = self._get_id_path('folders')
		response = self._GET(path,kwargs)
		return response


	def issueDetails(self,id=None,**kwargs):
		path = self._get_id_path('issueDetails')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def issueTemplates(self,id=None,**kwargs):
		path = self._get_id_path('issueTemplates')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def issueaging(self,**kwargs):
		path = self._get_id_path('issueaging')
		response = self._GET(path,kwargs)
		return response

	def issueaginggroup(self,**kwargs):
		path = self._get_id_path('issueaginggroup')
		response = self._GET(path,kwargs)
		return response


	def issuesAuditHistory(self,parent_id,**kwargs):
		path = self._get_id_path('issues')
		path = '{0}/{1}/auditHistory'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def issuesComments(self,parent_id,**kwargs):
		path = self._get_id_path('issues')
		path = '{0}/{1}/comments'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def jobs(self,id=None,**kwargs):
		path = self._get_id_path('jobs')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def jobsWarnings(self,parent_id,**kwargs):
		path = self._get_id_path('jobs')
		path = '{0}/{1}/warnings'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response


	def ldapObjects(self,id=None,**kwargs):
		path = self._get_id_path('ldapObjects')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def localUsers(self,id=None,**kwargs):
		path = self._get_id_path('localUsers')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def performanceIndicators(self,id=None,**kwargs):
		path = self._get_id_path('performanceIndicators')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def permissions(self,id=None,**kwargs):
		path = self._get_id_path('permissions')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def permissionsDependsOn(self,parent_id,**kwargs):
		path = self._get_id_path('permissions')
		path = '{0}/{1}/dependsOn'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def personas(self,id=None,**kwargs):
		path = self._get_id_path('personas')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def portlets(self,**kwargs):
		path = self._get_id_path('portlets')
		path = '{0}/issueaging'.format(path)
		response = self._GET(path,kwargs)
		return response

	def projectVersions(self,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsArtifacts(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/artifacts'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsAttributes(self,parent_id,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/attributes'.format(path,str(parent_id))
		if id is not None:
			path = path + '/' + str(id)
		response = self._GET(path,kwargs)
		return response

	def projectVersionsAuditAssistantStatus(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/auditAssistantStatus'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsAuditAssistantTrainingStatus(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/auditAssistantTrainingStatus'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsAuthEntities(self,parent_id,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/authEntities'.format(path,str(parent_id))
		if id is not None:
			path = path + '/' + str(id)
		response = self._GET(path,kwargs)
		return response

	def projectVersionsBugfilingrequirements(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/bugfilingrequirements'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsBugtracker(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/bugtracker'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsFilterSets(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/filterSets'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsIssueGroups(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/filterSets'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsIssueSearchOptions(self,parent_id,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/issueSearchOptions'.format(path,str(parent_id))
		if id is not None:
			path = path + '/' + str(id)
		response = self._GET(path,kwargs)
		return response

	def projectVersionsIssueSelectorSet(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/issueSelectorSet'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsIssueSummaries(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/issueSelectorSet'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response


	def projectVersionsIssues(self,parent_id,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/issues'.format(path,str(parent_id))
		if id is not None:
			path = path + '/' + str(id)
		response = self._GET(path,kwargs)
		return response

	def projectVersionsPerformanceIndicatorHistories(self,parent_id,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/performanceIndicatorHistories'.format(path,str(parent_id))
		if id is not None:
			path = path + '/' + str(id)
		response = self._GET(path,kwargs)
		return response

	def projectVersionsResponsibilities(self,parent_id,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/responsibilities'.format(path,str(parent_id))
		if id is not None:
			path = path + '/' + str(id)
		response = self._GET(path,kwargs)
		return response

	def projectVersionsResultProcessingRules(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/resultProcessingRules'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsSourceFiles(self,parent_id,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/sourceFiles'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def projectVersionsVariableHistories(self,parent_id,id=None,**kwargs):
		path = self._get_id_path('projectVersions')
		path = '{0}/{1}/variableHistories'.format(path,str(parent_id))
		if id is not None:
			path = path + '/' + str(id)
		response = self._GET(path,kwargs)
		return response

	def projects(self,id=None,**kwargs):
		path = self._get_id_path('projects')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def reportDefinitions(self,id=None,**kwargs):
		path = self._get_id_path('reportDefinitions')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def reportLibraries(self,id=None,**kwargs):
		path = self._get_id_path('reportLibraries')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def reports(self,id=None,**kwargs):
		path = self._get_id_path('reports')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def roles(self,id=None,**kwargs):
		path = self._get_id_path('roles')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def rolesPermissions(self,parent_id,**kwargs):
		path = self._get_id_path('roles')
		if id is not None:
			path = '{0}/{1}/permissions'.format(path,str(parent_id))
		response = self._GET(path,kwargs)
		return response

	def scans(self,id,**kwargs):
		path = self._get_id_path('scans')
		path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response

	def variables(self,id=None,**kwargs):
		path = self._get_id_path('variables')
		if id is not None:
			path = '{0}/{1}'.format(path,str(id))
		response = self._GET(path,kwargs)
		return response


	def updateRulepacks(self,**kwargs):
		path = self._get_id_path('updateRulepacks')
		response = self._GET(path,kwargs)
		return response

	def userSessionState(self,**kwargs):
		path = self._get_id_path('userSession') + '/state'
		response = self._GET(path,kwargs)
		return response

	def validateSearchString(self,**kwargs):
		path = self._get_id_path('validateSearchString')
		response = self._GET(path,kwargs)
		return response
