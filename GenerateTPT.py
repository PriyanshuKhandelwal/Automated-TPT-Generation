import pandas as pd
import sys
import os
import datetime
try:
    print("Enter datasheet name in .csv format:")
    datasheet_name = str(input())
    if ".csv" in datasheet_name:
        idatasheet_name = datasheet_name
    else:
        idatasheet_name = datasheet_name+"{}".format(".csv")
    idatasheet = pd.read_csv(idatasheet_name)
    #print(datasheet)
    datasheet = idatasheet.dropna()
    #print(datasheet)
    
    now = datetime.datetime.now()
    foldername = now.strftime("%d%b%Y_%H_%M_%S")
    os.mkdir(foldername)
    print("\n")
    print("********************************************************")
    print("Target folder for TPT files is : {}".format(foldername))
    print("********************************************************")
    print("\n")
except:
    print("ERROR : Incorrect file name or file doesn't exist")
    #quit()
#Temporary Variables############################################################33
#col_name_list= ["column1","column2","column3","column4","column5","column1","column2","column3","column4","column5","column1","column2","column3","column4","column5"]

#All variables declared here********************************TAKE CARE OF INDENTATION*****************************************
def TPT_generation(index):
        Load_DBName = datasheet["varLoad_DBName"][index]
        Export_DBName = datasheet["varExport_DBName"][index]
        SchemaName = datasheet["varSchemaName"][index]
        Export_PrivateLogName = datasheet["varExport_PrivateLogName"][index]
        Export_MaxSessions = datasheet["varExport_MaxSessions"][index]
        Export_MinSessions = datasheet["varExport_MinSessions"][index]
        Export_TdpID = datasheet["varExport_TdpID"][index]
        Export_UserName = datasheet["varExport_UserName"][index]
        Export_UserPassword = datasheet["varExport_UserPassword"][index]
        Export_SelectStmt = datasheet["varExport_SelectStmt"][index]
        Export_Dateform = datasheet["varExport_Dateform"][index]
        Load_PrivateLogName = datasheet["varLoad_PrivateLogName"][index]
        Load_MaxSessions = datasheet["varLoad_MaxSessions"][index]
        Load_MinSessions = datasheet["varLoad_MinSessions"][index]
        Load_TargetTable_suffix = datasheet["varLoad_TargetTable_suffix"][index]
        Load_TargetTable = "{}._{}{}".format(Load_DBName,SchemaName,Load_TargetTable_suffix)
        Load_TdpID = datasheet["varLoad_TdpID"][index]
        Load_UserName = datasheet["varLoad_UserName"][index]
        Load_UserPassword = datasheet["varLoad_UserPassword"][index]
        Load_ErrorTable1_suffix = datasheet["varLoad_ErrorTable1_suffix"][index]
        Load_ErrorTable1 = "{}._{}{}".format(Load_DBName,SchemaName,Load_ErrorTable1_suffix)
        Load_ErrorTable2_suffix = datasheet["varLoad_ErrorTable2_suffix"][index]
        Load_ErrorTable2 = "{}._{}{}".format(Load_DBName,SchemaName,Load_ErrorTable2_suffix)
        Load_LogTable_suffix = datasheet["varLoad_LogTable_suffix"][index]
        Load_LogTable = "{}._{}{}".format(Load_DBName,SchemaName,Load_LogTable_suffix)
        filename = "{}/TPT_{}.txt".format(foldername,SchemaName)
        view_filename = datasheet["varViewFileName"][index]
         
        
        #by developer
        #To edit number of spaces
        def_spaces = 100
        #To edit default varchar value
        def_varchar = 30
        #ENDS HERE
        
        ##############Gets column names from VIEW#########################
        def col_name_list(view_filename=view_filename):
            if ".txt" in view_filename:
                txtfilename = view_filename
            else:
                txtfilename = view_filename+"{}".format(".txt")
            
            try :
                view = open(txtfilename,"r") 
                mystring = view.read()
                mylist = mystring.split()
                index = -1

                for word in mylist:
                    index +=1
                    word_upper = word.upper()
                    if word_upper=="SELECT":
                        select_index = index
                    if word_upper=="FROM":
                        from_index = index

                mynewlist = mylist[select_index+1:from_index]
                final_list = []
                for word in mynewlist:
                    word = word.replace(",","").strip()
                    final_list.append(word)
                return final_list
            
    
            except FileNotFoundError:
                print("{}: No such file exist".format(txtfilename))
            
            
    #########################END#################################
    
    #Various Format(s) are added here**************************TAKE CARE OF INDENTATION****************************************************************
        def format1(_list):
            first_name = _list[0]
            remaining_names = _list[1:]
            number_of_loops = len(_list)-1
            format1_i = first_name.rjust(def_spaces-12)+" VARCHAR({})".format(def_varchar)
            style_print(format1_i)
            for col_name in remaining_names:
                added_comma = ","+ col_name+" VARCHAR({})".format(def_varchar)
                added_r_spaces = added_comma.rjust(def_spaces)
                style_print(added_r_spaces)
    
    
        def format2(_list):
            first_name = _list[0]
            first_name_edit = "CAST ("+ first_name
            remaining_names = _list[1:]
            number_of_loops = len(_list)-1
            format1_i = first_name_edit.rjust(def_spaces-13)+" AS "+" VARCHAR({})".format(def_varchar)+")"
            style_print(format1_i)
            for col_name in remaining_names:
                added_comma = ","+"CAST ("+ col_name+" AS "+" VARCHAR({})".format(def_varchar)+")"
                added_r_spaces = added_comma.rjust(def_spaces)
                style_print(added_r_spaces)
    	
    	
        def format3(_list):
            first_name = _list[0]
            remaining_names = _list[1:]
            style_print(" "+first_name)
            for col_name in remaining_names:
                style_print("{}".format(",")+col_name)
        	
        	
        def format4(_list):
            first_name = _list[0]
            remaining_names = _list[1:]
            style_print(" :"+first_name)
            for col_name in remaining_names:
                style_print("{}{}".format(",",":")+col_name)
    	
    	
    
            
        def Attribute_Format(datatype, varname,value,comma = True):
            if(comma):
                style_print("{}".format(datatype.rjust(10))+" "+"{}".format(varname)+" = "+"{},".format(convert_to_int(value)))
            else:
                style_print("{}".format(datatype.rjust(10))+" "+"{}".format(varname)+" = "+"{}".format(convert_to_int(value)))
    	
    #ENDS HERE
    
    
    		
    #Internal code begins here: *************************TAKE CARE OF INDENTATION*******************************************
    
        def DEFINE_SCHEMA(SchemaName = SchemaName):
            _list = col_name_list()
            style_print("DEFINE SCHEMA Schema_"+"{}".format(SchemaName))
            style_print("(")
            #FUNCTION CALL: format1()
            format1(_list)
            style_print(");")
        	
        def DEFINE_OPERATOR_EXPORT(SchemaName = SchemaName ,Export_DBName = Export_DBName):
            _list = col_name_list()
            style_print("DEFINE OPERATOR export_"+"{}".format(SchemaName)+
                    "\nTYPE EXPORT"+
                    "\nSCHEMA Schema_{}".format(SchemaName))
            style_print("ATTRIBUTES")
            style_print("(")
            EXPORT_LOL = [['VARCHAR', 'PrivateLogName',Export_PrivateLogName],
                          ['INTEGER', 'MaxSessions',Export_MaxSessions],
                          ['INTEGER', 'MinSessions', Export_MinSessions],
                          ['VARCHAR', 'TdpID',Export_TdpID],
                          ['VARCHAR', 'UserName', Export_UserName],
                          ['VARCHAR', 'UserPassword',Export_UserPassword]
                         ]
            for ilist in EXPORT_LOL:
                Attribute_Format(ilist[0],ilist[1],ilist[2])
            
            style_print("{}".format("VARCHAR".rjust(10))+" "+"{}".format("SelectStmt")+" = "+"{}".format("'lock row for access SELECT"))
            format2(_list)
            style_print("FROM".rjust(48)+" "+"{}.{}".format(Export_DBName,SchemaName)+";',")
            Attribute_Format("VARCHAR","Dateform",Export_Dateform,comma=False)
            style_print(");")
    	
        def DEFINE_OPERATOR_LOAD(SchemaName = SchemaName ,Export_DBName = Export_DBName):
            style_print("DEFINE OPERATOR export_"+"{}".format(SchemaName)+
                    "\nTYPE LOAD"+
                    "\nSCHEMA Schema_{}".format(SchemaName))
            style_print("ATTRIBUTES")
            style_print("(")
            LOAD_LOL = [['VARCHAR', 'PrivateLogName',Load_PrivateLogName],
                          ['INTEGER', 'MaxSessions',Load_MaxSessions],
                          ['INTEGER', 'MinSessions', Load_MinSessions],
                          ['VARCHAR', 'TargetTable' , Load_TargetTable],
                          ['VARCHAR', 'TdpID',Load_TdpID],
                          ['VARCHAR', 'UserName', Export_UserName],
                          ['VARCHAR', 'UserPassword',Export_UserPassword],
                          ['VARCHAR', 'ErrorTable1',Load_ErrorTable1],
                          ['VARCHAR', 'ErrorTable2',Load_ErrorTable2],
                         ]
            for ilist in LOAD_LOL:
                Attribute_Format(ilist[0],ilist[1],ilist[2])
            
            #style_print("{}".format("VARCHAR".rjust(10))+" "+"{}".format("SelectStmt")+" = "+"{}".format("'lock row for access SELECT"))
            #format2()
            #style_print("FROM".rjust(48)+" "+"{}.{}".format(Export_DBName,SchemaName)+";',")
            Attribute_Format("VARCHAR","LogTable",Load_LogTable,comma=False)
            style_print(");")
           
        def APPLY_and_VALUES(_list=col_name_list):
            _list = col_name_list()
            style_print("APPLY ('")
            insert_string = "INSERT INTO "+Load_TargetTable
            style_print("(")
            format3(_list)
            style_print(")")
            style_print("VALUES(")
            format4(_list)
            style_print(")")
            style_print("')")
    	
        def START(index):
            start_string = "DEFINE JOB EXPORT_Load_{}".format(SchemaName)
            style_print(start_string)
            style_print("(")
            DEFINE_SCHEMA()
            DEFINE_OPERATOR_EXPORT()
            DEFINE_OPERATOR_LOAD()
            APPLY_and_VALUES()
            insert_newline()
            style_print("TO OPERATOR (")
            load_SchemaName = "Load_{}[1]".format(SchemaName)
            style_print(load_SchemaName.rjust(5))
            style_print(")".rjust(30))
            insert_newline()
            select_statement = "SELECT * FROM OPERATOR (export_{}[1])".format(SchemaName)
            style_print(select_statement)
            style_print(");")
    	#print("{} generated successfully!")
    #ENDS HERE
    	
    #SOME Additional functions begins here*******************TAKE CARE OF INDENTATION***********************************
        def insert_newline():
            style_print("\n")
        	
        def convert_to_int(word):
            try:
                return(int(word))
            except:
                return("'"+word+"'")
        def style_print(input_txt, mode = "a"):
            f = open(filename,mode)
            f.write(input_txt+"\r")
            f.close()
        
        START(index)
    
def run():
    loop_count = datasheet.shape[0]
    i = 0
    for i in range(loop_count):
        TPT_generation(i)
        file_count=i+1
        SchemaName = datasheet["varSchemaName"][i]
        print("{}) TPT generated for Schema Name: {}".format(file_count,SchemaName))
    print("Total TPT generated: {}".format(i+1))
    print("Not generated TPT:   {} ".format(loop_count - i-1))


try:
    #print("\n")
    print("********************************************************")
    print(".............processing")
    #print("\n")
    run()
    print("\n")
    print("********************************************************")
    print("COMPLETED! Please check files in folder '{}'".format(foldername))
    print("********************************************************")
    print("\n")
except Exception:
    print("\n")
    print("********************************************************")
    print("ERROR OCCURED :( ")
    print("Please check if all the column values are filled")
    print("********************************************************")
    print("\n")
    print("\n")
    print("© www.tcs.com")