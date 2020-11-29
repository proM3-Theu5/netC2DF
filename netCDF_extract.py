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

# Getting variables with 3 Dimensions
var_3d_dim = list(variables_df[variables_df['Dims_len'] == 3]['Variable'])

# Generating dataframes for 3d variables
var_3d_df_dict = {}
for var_3d in var_3d_dim:
    # Getting the array out
    array_3d = ma.getdata(nc_f.variables[var_3d][:,:,:])
    dim_1_size,dim_2_size,dim_3_size = array_3d.shape
    dim_1_name,dim_2_name,dim_3_name = variables_df[variables_df['Variable'] == var_3d]['Dimensions'].values[0]
    reshape_tuple = array_3d.shape[1:3]
    # Generating datasets by keeping 1st dim as constant
    df_3d_dict = {}
    for dim_1_ix in range(dim_1_size):
        temp_df = pd.DataFrame(data = ma.getdata(nc_f.variables[var_3d][dim_1_ix:dim_1_ix+1,:,:].reshape(reshape_tuple)))
        temp_df.insert(0,dim_2_name,temp_df.index) 
        temp_df[dim_2_name] = dim_2_name+'_'+temp_df[dim_2_name].astype('str')
        temp_df.insert(0,dim_1_name,dim_1_name+'_'+str(dim_1_ix))
        df_3d_dict[str(dim_1_ix)] = temp_df
    # Merging the dataframe together
    df_list = [df_3d_dict[key] for key in df_3d_dict]
    df_3d_var = pd.concat(df_list, ignore_index=True)
    var_3d_df_dict[var_3d] = df_3d_var


# Getting the variables with 1 dimension
var_1d_dim = list(variables_df[variables_df['Dims_len'] == 1]['Variable'])

# Generating the single dimension names for these variables
variables_1d_df = variables_df[variables_df['Dims_len'] == 1]
variables_1d_df['Dimension_1d'] = [dim[0] for dim in variables_1d_df['Dimensions']]
variables_1d_df['Dimension_1d'] = variables_1d_df['Dimension_1d'].astype('str')

# Getting the unique 1d dimesion values
var_1d_dims = variables_1d_df['Dimension_1d'].unique()

# Getting the variables for each dimensions
var_v_dim_dict = {}
for dim in var_1d_dims:
    var_v_dim_dict[dim] = list(variables_1d_df[variables_1d_df['Dimension_1d'] == dim]['Variable'])

# Getting dataframes for 1d variables
var_1d_df_dict = {}
for dim in var_v_dim_dict:
    temp_df = pd.DataFrame()
    for var in var_v_dim_dict[dim]:
        temp_df[var] = ma.getdata(nc_f.variables[var][:])
    var_1d_df_dict[dim] = temp_df