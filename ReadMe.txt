Pre-Requisites:

1. Python IDE
2. Python modules - streamlit, plotly, json, mysql-connector-python.
3. Git Software - Download link : https://git-scm.com/download/

How to run it?

1. Download the Repo files as zip file(PhonePe).
2. Extract the zip file.
3. In the extracted folder "main.py" is the main file other files are subfiles which has function defined to do certain task
4. Open command prompt and move towards the directory where the main file and other sub-files are located.
5. Run the command "streamlit run main.py" or "streamlit run .\main.py" in the command prompt after moving towards the files directory.
6. A page will be loaded in the browser or in command prompt or we can manually open the page by accessing the link which will be displayed in the command prompt.

Program Files:
1. main.py
	*It is the main file of the project
	*It will have a function "run_once()" which will be executed only once.
	*It will call other functions "clone.Clone(), DataBase.main()"
	*The main file will shows the option for choosing the data for visualization.
	*After getting the options it calls other functions "Get_Data.GetData" and smap.Map(df,s,data)
	*It also tabulates the data.

2. clone.py
	*It will clone the dataset from git repo
	*Store the cloned data in the same directory where the python files are stored

3. DataBase.py
	*It has two funtions "main():", "create_database():" and "store_files(directory_path):"
	*The "main():" function will call "create_database():" and "store_files(directory_path):"
	*"create_database():" function will generally create a database named 'PhonePe' and a table in the database named 'storage'.
	*"store_files(directory_path):" will store the cloned data in the table
	*In table the first column contains the directory of json file second column contains the name of the file and third column contains the data in the file.

4. Get_Data.py
	*It has a function "GetData(data,year,month,Path):"
	*It will get the required data to create the path of the data file.
	*Using that it access the data from MySql is accessed.

5. smap.py:
	*"Map(df,s,data):" This function in smap.py will get the data to be plotted in India Map.
	*And It will load the datas in India map using the link of provided geojson file


Impotant Note:
	In both "DataBase.py" and "Get_Data.py" files you can find the below code
	
	connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Project',
            database='PhonePe'
        )

	or

	connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Project'
        )

	You have to replace 'root' with your user name in MySql and 'Project' with corresponding password of the user.
