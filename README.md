<h1 align="center">netC2DF</h1>
<p align='right'>A MORPH Project</p>
<hr>
<p align='center'>
<img src = 'https://img.shields.io/badge/SITUATION-SNAFU-blue'>
</p>
<hr>

<h2 align = 'center'><b>Introduction </b></h2>

><h3 align = 'left' padding-left = '10px'>What is <b>netC2DF</b>? </h3>
><p align = 'left'>netC2DF is a python based project to retrieve data from <b><i>netCDF</i></b> files. 
><br>
>This project has been implemented to provide with a generic script that could take any netCDF file as an input and generate the data and metadata defined in the file as an output in various formats and data structures.</p>
<br>


><h3 align = 'left' padding-left = '10px'>What is <b>netCDF</b>? </h3>
><p align = 'left'> Full Form : <b>Network Common Data Form</b>
><p align = 'left'> NetCDF (Network Common Data Form) is a set of software libraries and machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. It is also a community standard for sharing scientific data.</p>
<br>


><h3 align = 'left' padding-left = '10px'>Why <b>netCDF</b>? </h3>
><p align = 'left'> This format has many advantages, the most important of which is that it is <i>self-describing</i>, meaning that software packages can directly read the data and determine its structure, the variable names and essential metadata such as the units.</p>
<br>

<hr>
<h2 align = 'center'> Purpose </h2>

><h3 align = 'left'>Requirement</h3>
><p align = 'left'> A quick and handy way to retrieve data from any netCDF format data files into required formats</p>
><br>
><h3 align = 'left'>Solution</h3>
><p align = 'center' style="font-size:1.5em;" > <b>netC2DF</b></p>
><hr>

<hr>
<h2 align = 'center'> MOTIVATION </h2>
<br>

><p>netCDF is a commonly used file for scientific data which is being used aggressively by individuals and groups dealing with scientific projects and studies.
><br>
>Most of such projects require a specific modelling and visualization tool.
><br>
>This project has been initiated to provide an ease of connection between netCDF data and such tools used widely.</p>

<hr>
<h2 align = 'center'>Future of the Project</h2>
<br>

>1.  Python Script to generate DataFrames from the data and metadata from the netCDF files
><img src = 'https://img.shields.io/badge/STAGE-Current-9cf' align = 'right'>
>
>2. Generate excel file with the DataFrames generated with proper naming
><img src = 'https://img.shields.io/badge/STAGE-Future-red' align = 'right'>
>
>3. Integrate the python script results with other tools (Vizualization, Analytics , Modelling …)
><img src = 'https://img.shields.io/badge/STAGE-Future-red' align = 'right'>
><br>

<hr>
<h2 align = 'center'>Programming Language</h2>
<br>
<p align='center' style="font-size:1.5em;"><b>PYTHON</b></p>

><h3 align = 'left'><b>Modules Used</b></h3>
><br>

>1.	**netCDF4** – For reading the netCDF files
>2.	**pandas** – For storing and transforming the datasets generated from the files
>3.	**numpy** – For reading the scientific data and retaining the data integrity
><br>
><br>

><h3 align = 'left'><b>Features</b></h3>
><br>
>
>1.	Generate a DataFrame with the details of the metadata of the netCDF file
>2.	Generate DataFrames for 1D , 2D and 3D datasets available in the netCDF file
>3.	Conolidate the DataFrames into dictionaries, with the variable names as keys
><br>
><br>

<hr>
<h2 align = 'center'>How To User</h2>
<br>

><h3 align = 'right'><b>Pre-Requisites</b></h3>

>1.	Python installed on the machine
>2.	Following modules to be installed :

            pip install netCDF4
            pip install pandas  
            pip install numpy

><h3 align = 'right'><b>Stes to Use</b></h3>

>1.	Place the Python Script in a local directory
>2.	Place the netCDF data source file in the same directory as the python script
>3.	Open the Python script in a text editor
>4.	Update the value for file_path variable with the required filename
>5.	Save the updated script
>6.	Open a Commandline window
>7.	Navigate to the directory where the python script is stored on the commandline window
>8.	Execute – python script.py
