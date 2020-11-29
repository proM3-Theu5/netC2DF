import netCDF4
import numpy as np
import pandas as pd
import numpy.ma as ma

# Reading the netCDF4 file
nc_f = netCDF4.Dataset('AOI_OID54761_SRL_GPS_2PTP128_0998_20190415_124731_20190415_133750.CNES.nc')

# Getting the global attributes
nc_attrs = nc_f.ncattrs()

# # Getting details of nc attrs
# for nc_attr in nc_attrs:
#     print(nc_attr,':',nc_f.getncattr(nc_attr))

# Generating the dataframe for Global Attributes
global_attr = nc_f.ncattrs()
attr_values = [nc_f.getncattr(nc_attr) for nc_attr in nc_attrs]
global_attr_df = pd.DataFrame(columns = ['Attribute','Value'], data = zip(global_attr,attr_values)) 

# Getting the dimensions
dim_dict = nc_f.dimensions
dim_keys = list(dim_dict.keys())
dim_size = [dim_dict[key].size for key in dim_keys]

# Generating the dataframe for Global Attributes
global_attr = nc_f.ncattrs()
attr_values = [nc_f.getncattr(nc_attr) for nc_attr in nc_attrs]
global_attr_df = pd.DataFrame(columns = ['Attribute','Value'], data = zip(global_attr,attr_values))

# Getting the dimensions
dim_dict = nc_f.dimensions
dim_keys = list(dim_dict.keys())
dim_size = [dim_dict[key].size for key in dim_keys]

# Generating the dataframe for Dimensions
dimensions_df = pd.DataFrame(columns = ['Dimension','Size'], data = zip(dim_keys,dim_size))

# Getting the variables
nc_vars = [var for var in nc_f.variables]
nc_dims = [nc_f.variables[var].dimensions for var in nc_vars]
nc_types = [nc_f.variables[var].dtype for var in nc_vars]

# Generating the dataframe for Variables
variables_df = pd.DataFrame(columns = ['Variable','Type','Dimensions'], data = zip(nc_vars,nc_types,nc_dims))
variables_df['Dims_str'] = variables_df['Dimensions'].astype('str')
variables_df['Dims_len'] = variables_df['Dimensions'].apply(lambda x: len(x))

# Getting the variable with dimensions 1

var_x_dim = list(variables_df[variables_df['Dims_str'] == "('x',)"]['Variable'])
var_y_dim = list(variables_df[variables_df['Dims_str'] == "('y',)"]['Variable'])
var_z_dim = list(variables_df[variables_df['Dims_str'] == "('z',)"]['Variable'])

# Generating dataframe for single dimensions
x_var_df = pd.DataFrame()
y_var_df = pd.DataFrame()
z_var_df = pd.DataFrame()

for x_var in var_x_dim:
    x_var_df[x_var] = ma.getdata(nc_f.variables[x_var][:])

for y_var in var_y_dim:
    y_var_df[y_var] = ma.getdata(nc_f.variables[y_var][:])

for z_var in var_z_dim:
    z_var_df[z_var] = ma.getdata(nc_f.variables[z_var][:])

# Getting variables with 2 dimesions
var_2d_dim = list(variables_df[variables_df['Dims_len'] == 2]['Variable'])

# Generating dataframe for 2 d variables
var_2d_df_dict = {}
for var_2d in var_2d_dim:
    row_pref = variables_df[variables_df['Variable'] == var_2d]['Dimensions'].values[0][0]
    col_pref = variables_df[variables_df['Variable'] == var_2d]['Dimensions'].values[0][0]
    temp_df = pd.DataFrame(data = ma.getdata(nc_f.variables[var_2d][:,:]))
    temp_df.columns = [str(col_pref) + str(col) for col in temp_df.columns]
    temp_df.set_index(str(row_pref) + temp_df.index.astype(str))
    var_2d_df_dict[var_2d] = temp_df