PyFortify
=====

A Python interface for the Fortify API.

The goal of this library is to map Fortify endpoints one-to-one. Calls to Fortify are made with clean, Pythonic methods. 

Dependencies:

- requests


Installation
------------

Install via pip:

.. code-block:: bash

    To Do

Install from source:

.. code-block:: bash

   To Do
   
Usage
-----

Import the module:

.. code-block:: bash

    import PyFortify

Instantiating a client:

.. code-block:: bash

    FClient = PyFortify.Connect()

Examples
--------

**Activity-feed-events**: Retrieve list of activity feed entries 

.. code-block:: bash

    >>> FClient.activityFeedEvents() 

**Alert-definitions**: Alert definitions management 

.. code-block:: bash

    >>> FClient.alertDefinitions() 

To fetch a particular alert defination:

.. code-block:: bash

    >>> FClient.alertDefinitions('parent_id') 

**Alertable-event-types**: Retrieve the list of event types for which alerts can be created 

.. code-block:: bash

    >>> FClient.alertableEventTypes() 

**Alerts**: Retrieve list of fired alerts 

.. code-block:: bash

    >>> FClient.alerts() 

**Attribute-definitions**: Attribute definitions management 

.. code-block:: bash

    >>> FClient.attributeDefinitions() 

**Authentication-entities**: Retrieve aggregated list of local and LDAP user accounts that have been set up in SSC (LDAP Groups can be accessed via a linked resource)

.. code-block:: bash

    >>> FClient.authEntities() 

**Authentication-entity-roles**: Retrieve list of Roles for the specific Auth Entity 

.. code-block:: bash

    >>> FClient.authEntitiesRoles('parent_id') 

**Ldap-authentication-entity-groups**: Retrieve list of the LDAP Groups for the specified LDAP Auth Entity 

.. code-block:: bash

    >>> FClient.authEntitiesGroups('parent_id') 

**Bugfield-template-groups**: Bugfield template groups management 

.. code-block:: bash

    >>> FClient.bugfieldTemplateGroups() 


**Bug-trackers**: Retrieve list of available bug trackers that have been set up in SSC 

.. code-block:: bash

    >>> FClient.bugtrackers() 

**Api-bulk-request-controller**: Api Bulk Request Controller 

.. code-block:: bash

    >>> FClient.bulk() 

**Bugfield-template-groups**: Bugfield template groups management 

.. code-block:: bash

    >>> FClient.bugfieldTemplateGroups() 

**Cloudscan-jobs**: Cloudscan jobs monitoring 

.. code-block:: bash

    >>> FClient.cloudjobs() 

**Cloudscan-pools**: Cloudscan pools management 

.. code-block:: bash

    >>> FClient.cloudPools() 

**Cloudscan-jobs-for-cloudscan-pool**: Cloudscan jobs for Cloudscan pool management 

.. code-block:: bash

    >>> FClient.cloudpoolsJobs('parent_id')

**Project-versions-for-cloudscan-pool**: Project versions for Cloudscan pool management

- Versions

.. code-block:: bash

    >>> FClient.cloudpoolsVersions('parent_id')

- Versions/action

.. code-block:: bash

    >>> FClient.cloudpoolsVersionsAction('parent_id')


**Cloudscan-workers-for-cloudscan-pool**: Cloudscan workers for Cloudscan pool management 

.. code-block:: bash

    >>> FClient.cloudpoolsWorkersAction('parent_id')


**Cloudscan-system**: Cloudscan system information 

- Metrics

.. code-block:: bash

    >>> FClient.cloudsystemMetrics() 
- Pollstatus

.. code-block:: bash

    >>> FClient.cloudsystemPollstatus() 
- Settings

.. code-block:: bash

    >>> FClient.cloudsystemsettings() 

**Cloudscan-workers**: Cloudscan workers monitoring 

.. code-block:: bash

    >>> FClient.cloudpoolsWorkers('parent_id') 

**Cloudscan-worker-jobs**: Cloudscan jobs by worker monitoring

.. code-block:: bash

    >>> FClient.cloudworkersCloudjobs('parent_jobs') 

**Disabled-cloudscan-workers**: List of Cloudscan workers that are not assigned to any Cloudscan pool 

.. code-block:: bash

    >>> FClient.cloudPoolsDisabledWorkers() 

**Core-rulepacks**: Rulepacks management 

.. code-block:: bash

    >>> FClient.coreRulepacks 


**Custom-tags**: Custom tags definition management 

.. code-block:: bash

    >>> FClient.customTags() 

**Engine-type-controller**: Engine Type Controller 

.. code-block:: bash

    >>> FClient.engineTypes() 

**Events**: Retrieve the list of SSC application event logs 

.. code-block:: bash

    >>> FClient.events() 

**File-tokens**: Retrieve a file token for various file upload and download operations 

.. code-block:: bash

    >>> FClient.fileTokes() 

**Folders**: Retrieve a list of defined folders attributeDefinitions

.. code-block:: bash

    >>> FClient.folders() 

**Issue-details**: Retrieve detailed information about the issue 

.. code-block:: bash

    >>> FClient.issueDetails() 

**Issue-templates**: Issue templates management 

.. code-block:: bash

    >>> FClient.issueTemplates() 

**Issue-aging**: Endpoint for getting precalculated issue aging metrics. 

.. code-block:: bash

    >>> FClient.issueaging() 

**Issue-aging-group**: Endpoint for getting all possible values for specific group attribute for issue aging table. 

.. code-block:: bash

    >>> FClient.issueaginggroup() 

**Issue-audit-history**: Retrieve the list of audit history events for the specific issue 

.. code-block:: bash

    >>> FClient.issuesAuditHistory() 

**Issue-comments**: Retrieve the list of the issue comments and add new comment to the issue 

.. code-block:: bash

    >>> FClient.issuesComments() 

**Jobs**: Retrieve the list of the jobs in the queue and update limited number of job attributes. 

.. code-block:: bash

    >>> FClient.jobs 

**Job-priority-change-warnings**: Obtain a list of warnings what would happen if user changed job priority 

.. code-block:: bash

    >>> FClient.jobsWarnings('parent_id') 

**Ldap-objects**: LDAP objects management 

.. code-block:: bash

    >>> FClient.ldapObjects() 

**Local-users**: Local users management 

.. code-block:: bash

    >>> FClient.localUsers() 

**Performance-indicators**: Performance indicators management 

.. code-block:: bash

    >>> FClient.performanceIndicators() 

**Permissions**: Retrieve list of permissions and permission details for the specific permission GUID 

.. code-block:: bash

    >>> FClient.permissions() 

**Permissions-depends-on**: Retrieve the list of permissions that this permission depends on 

.. code-block:: bash

    >>> FClient.permissionsDependsOn('parent_id') 

**Personas**: Personas management 

.. code-block:: bash

    >>> FClient.personas() 

**Issue-aging-portlet**: Retrieve issue aging portlet 

.. code-block:: bash

    >>> FClient.portlets() 

**Project-version-artifacts**: Retrieve list of the FPR artifacts associated with this project version. 

.. code-block:: bash

    >>> FClient.projectVersionsArtifacts('parent_id') 

**Project-version-attributes**: Project version attributes management. 

.. code-block:: bash

    >>> FClient.projectVersionsAttributes('parent_id') 

**Project-version-audit-assistant-status-controller**: Project Version Audit Assistant Status Controller 

.. code-block:: bash

    >>> FClient.projectVersionsAuditAssistantStatus('parent_id') 

**Project-version-authentication-entities**: Retrieve list of the authentication entities associated with this project version. 

.. code-block:: bash

    >>> FClient.projectVersionsAuthEntities('parent_id') 


**Project-version-bug-filing-requirements**: The bug filing requirements (various bug params, is Authentication required) management for the bugtracker plugin associated with this project version 

.. code-block:: bash

    >>> FClient.projectVersionsBugfilingrequirements('parent_id') 

**Project-version-bug-trackers**: Retrieve or change bugtracker assigned to the project version 

.. code-block:: bash

    >>> FClient.projectVersionsBugtracker('parent_id') 

**Project-version-filter-sets**: Retrieve the list of filter sets defined for the project version 

.. code-block:: bash

    >>> FClient.projectVersionsFilterSets('parent_id') 

**Project-version-issue**: Retrieve the list of issues in the project version 

.. code-block:: bash

    >>> FClient.projectVersionsIssues('parent_id') 

**Project-version-issue-groups**: Retrieve the list of issue groups in the project version 

.. code-block:: bash

    >>> FClient.projectVersionsIssueGroups('parent_id') 

**Project-version-issue-search-options**: Retrieve and change issues search options for the specific project version 

.. code-block:: bash

    >>> FClient.projectVersionsIssueSearchOptions('parent_id') 

**Project-version-issue-selector-set**: Retrieve list of all possible issue grouping and filtering options for the project version 

.. code-block:: bash

    >>> FClient.projectVersionsIssueSelectorSet('parent_id') 

**Project-version-issue-summaries**: Retrieve performance indicators values history for the specific project version 

.. code-block:: bash

    >>> FClient.projectVersionsIssueSummaries('parent_id') 

**Project-version-performance-indicator-histories**: Retrieve performance indicators values history for the specific project version 

.. code-block:: bash

    >>> FClient.projectVersionsPerformanceIndicatorHistories('parent_id') 

**Project-version-responsibilities**: Project version responsibilities management. 

.. code-block:: bash

    >>> FClient.projectVersionsResponsibilities('parent_id') 

**Project-version-result-processing-rules**: Retrieve artifacts processing rules for the specific project version and changing values of these rules 

.. code-block:: bash

    >>> FClient.projectVersionsResponsibilities('parent_id') 

**Project-version-source-files**: Retrieve source files content where issues were found 

.. code-block:: bash

    >>> FClient.projectVersionsSourceFiles('parent_id') 

**Project-version-variable-histories**: Retrieve the history of variables for the project version 

.. code-block:: bash

    >>> FClient.projectVersionsVariableHistories('parent_id') 

**Project-versions**: Project versions management 

.. code-block:: bash

    >>> FClient.projects() 

**Report-definitions**: Report definitions management 

.. code-block:: bash

    >>> FClient.reportDefinitions() 

**Report-libraries**: Report libraries management 

.. code-block:: bash

    >>> FClient.reportLibraries() 

**Reports**: Reports management 

.. code-block:: bash

    >>> FClient.reports() 


**Role-associated-permissions**: permissions associated with a particular role 

.. code-block:: bash

    >>> FClient.rolesPermissions('parent_id') 

**Rulepacks-update**: Do rulepacks update 

.. code-block:: bash

    >>> FClient.updateRulepacks() 

**Scans**: Retrieve the detail about the scan by this scan ID 

.. code-block:: bash

    >>> FClient.scans() 

**User-roles**: User roles management. 

.. code-block:: bash

    >>> FClient.roles() 

**User-session-state**: Manage current user UI state 

.. code-block:: bash

    >>> FClient.userSessionState() 

**Validate-search-string**: Do search string validation 

.. code-block:: bash

    >>> FClient.validateSearchString() 

**Variables**: Variables management

.. code-block:: bash

    >>> FClient.variables() 
