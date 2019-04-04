# Automated-TPT-Generation
Python script to generate Teradata TPT format on local pc.
### Requirements: 
Python 3+

### Follow below mentioned steps:

1) Copy and save *schema structure* like shown below to a *file name.**txt*** :

`
SELECT
      column1,
      column2,
      column3, column4,
      column5,
      column6 ,column7,
      column8,
      column9,column9,column9,column9
column10,
column11
FROM
this is also normal text.`

**Note** down filename in the .csv file, which we will use in next step.
**********************************
2) Create a .csv file with name *GenerateTPT_csv.csv* and fill the following column values. Each row represent data corresponding to *.txt* file saved above


Column name| Description
------------|--------------
varLoad_DBName	|Supply_Chain_Core
varExport_DBName	|rslr_ops
varSchemaName	|name1
varExport_PrivateLogName	|exportoper_privatelog
varExport_MaxSessions	|5
varExport_MinSessions	|2
varExport_TdpID	|REDWOOD
varExport_UserName|c4994013
varExport_UserPassword	|Jan@2019
varExport_SelectStmt|		lock row for access SELECT
varExport_Dateform	|SampleExportDateform
varLoad_PrivateLogName|loadoper_privatelog
varLoad_MaxSessions	|5	
varLoad_MinSessions|2	
varLoad_TargetTable_suffix|	_UAT
varLoad_TdpID	| EDWUAT
varLoad_UserName|	supply_chain_user
varLoad_UserPassword|	new_supply_chain_pwd
varLoad_ErrorTable1_suffix|	_SchemaName_f1
varLoad_ErrorTable2_suffix|	_SchemaName_f2
varLoad_LogTable_suffix| _SchemaName_LT
varViewFileName|myfilename1

*********************************
3) Run **GenerateTPT.py** in the same folder location and pass .csv file name which was saved in above step.

> Your TPT files will be created in a auto-generated folder, whose name is as per the timestamp the code was run on.
