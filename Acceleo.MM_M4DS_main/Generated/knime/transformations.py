import os
import sys
from pathlib import Path

# Add the project's root to the python path
script_location = Path(__file__).absolute().parent
parent_directory = script_location.parent
sys.path.append(str(parent_directory))

import pandas as pd
import functions.data_transformations as data_transformations
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure
class DataProcessing:
	def generateDataProcessing(self):
		transformations=data_transformations.DataTransformations()
#-----------------New DataProcessing-----------------
		imputeByDerivedValue_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		imputeByDerivedValue_input_dataDictionary_transformed=data_dictionary.copy()
		
		missing_values_list=[]
		
		print('Special a Derived')
		imputeByDerivedValue_input_dataDictionary_transformed=transformations.transform_special_value_derived_value(data_dictionary=imputeByDerivedValue_input_dataDictionary_transformed,
																	  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																	  missing_values=missing_values_list,
																	  axis_param=0, field = 'sex')
		
		missing_values_list=[]
		
		print('Special a Derived')
		imputeByDerivedValue_input_dataDictionary_transformed=transformations.transform_special_value_derived_value(data_dictionary=imputeByDerivedValue_input_dataDictionary_transformed,
																	  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																	  missing_values=missing_values_list,
																	  axis_param=0, field = 'IRSCHOOL')
		
		missing_values_list=[]
		
		print('Special a Derived')
		imputeByDerivedValue_input_dataDictionary_transformed=transformations.transform_special_value_derived_value(data_dictionary=imputeByDerivedValue_input_dataDictionary_transformed,
																	  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																	  missing_values=missing_values_list,
																	  axis_param=0, field = 'ETHNICITY')
		
		imputeByDerivedValue_output_dataDictionary=imputeByDerivedValue_input_dataDictionary_transformed
		imputeByDerivedValue_output_dataDictionary.to_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		imputeByFixValue_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		imputeByFixValue_input_dataDictionary_transformed=data_dictionary.copy()
		
		missing_values_list=[]
		
		print('Special a Fix')
		imputeByFixValue_input_dataDictionary_transformed=transformations.transform_special_value_fix_value(data_dictionary=imputeByFixValue_input_dataDictionary_transformed,
																	  special_type_input=SpecialType(0), fix_value_output='Unknown',
																	  missing_values=missing_values_list,
								                                      data_type_output = DataType(0),
																	  axis_param=0, field = 'ACADEMIC_INTEREST_2')
		
		missing_values_list=[]
		
		print('Special a Fix')
		imputeByFixValue_input_dataDictionary_transformed=transformations.transform_special_value_fix_value(data_dictionary=imputeByFixValue_input_dataDictionary_transformed,
																	  special_type_input=SpecialType(0), fix_value_output='Unknown',
																	  missing_values=missing_values_list,
								                                      data_type_output = DataType(0),
																	  axis_param=0, field = 'ACADEMIC_INTEREST_1')
		
		imputeByFixValue_output_dataDictionary=imputeByFixValue_input_dataDictionary_transformed
		imputeByFixValue_output_dataDictionary.to_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		imputeByNumericOp_input_dataDictionary_transformed=data_dictionary.copy()
		
		missing_values_list=[]
		
		missing_values_list=[]
		
		imputeByNumericOp_output_dataDictionary=imputeByNumericOp_input_dataDictionary_transformed
		imputeByNumericOp_output_dataDictionary.to_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		imputeByNumericOp_input_dataDictionary_transformed=data_dictionary.copy()
		
		missing_values_list=[]
		
		imputeByNumericOp_output_dataDictionary=imputeByNumericOp_input_dataDictionary_transformed
		imputeByNumericOp_output_dataDictionary.to_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		rowFilter_input_DataDictionary=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		rowFilter_input_DataDictionary_transformed=data_dictionary.copy()
		
		
		
#-----------------New DataProcessing-----------------
		columnFilter_input_DataDictionary=pd.read_csv('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		columnFilter_input_DataDictionary_transformed=data_dictionary.copy()
		
		
#-----------------New DataProcessing-----------------
		mapping_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',')
		print('MAPPING')
		input_values_list=['A', 'N']
		output_values_list=['0', '0']
		data_type_input_list=[DataType(0), DataType(0)]
		data_type_output_list=[DataType(0), DataType(0)]
		
		
		mapping_output_dataDictionary=transformations.transform_fix_value_fix_value(data_dictionary=mapping_input_dataDictionary, input_values_list=input_values_list,
																	  output_values_list=output_values_list,
								                                      data_type_input_list = data_type_input_list,
								                                      data_type_output_list = data_type_output_list, field = 'TERRITORY')
		
		mapping_output_dataDictionary.to_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		mapping_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',')
		print('MAPPING')
		input_values_list=['Y', 'N']
		output_values_list=['1', '0']
		data_type_input_list=[DataType(0), DataType(0)]
		data_type_output_list=[DataType(0), DataType(0)]
		
		
		mapping_output_dataDictionary=transformations.transform_fix_value_fix_value(data_dictionary=mapping_input_dataDictionary, input_values_list=input_values_list,
																	  output_values_list=output_values_list,
								                                      data_type_input_list = data_type_input_list,
								                                      data_type_output_list = data_type_output_list, field = 'Instate')
		
		mapping_output_dataDictionary.to_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		categoricalToContinuous_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		categoricalToContinuous_input_dataDictionary_transformed=data_dictionary.copy()
		
		print('CategoricalToContinuous')
		categoricalToContinuous_input_dataDictionary_transformed=transformations.transform_cast_type(data_dictionary=categoricalToContinuous_input_dataDictionary_transformed,
																		data_type_output= DataType(6),
																		field_in=stringToNumber(TERRITORY)_input_dataField, field_out=stringToNumber(TERRITORY)_output_dataField)
		
		categoricalToContinuous_input_dataDictionary_transformed=transformations.transform_cast_type(data_dictionary=categoricalToContinuous_input_dataDictionary_transformed,
																		data_type_output= DataType(6),
																		field_in=stringToNumber(Instate)_input_dataField, field_out=stringToNumber(Instate)_output_dataField)
		
		categoricalToContinuous_output_dataDictionary=categoricalToContinuous_input_dataDictionary_transformed
		categoricalToContinuous_output_dataDictionary.to_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		imputeByNumericOp_input_dataDictionary_transformed=data_dictionary.copy()
		
		missing_values_list=[]
		
		missing_values_list=[]
		
		missing_values_list=[]
		
		imputeByNumericOp_output_dataDictionary=imputeByNumericOp_input_dataDictionary_transformed
		imputeByNumericOp_output_dataDictionary.to_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		binner_input_dataDictionary_transformed=data_dictionary.copy()
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																	  data_type_output = DataType(0),
																	  field_in = 'TOTAL_CONTACTS', field_out = 'TOTAL_CONTACTS_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																	  data_type_output = DataType(0),
																	  field_in = 'SELF_INIT_CNTCTS', field_out = 'SELF_INIT_CNTCTS_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																	  data_type_output = DataType(0),
																	  field_in = 'SOLICITED_CNTCTS', field_out = 'SOLICITED_CNTCTS_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=-1000.0, right_margin=1.0,
																	  closure_type=Closure(0),
																	  fix_value_output='low',
								                                      data_type_output = DataType(0),
																	  field_in = 'TOTAL_CONTACTS',
																	  field_out = 'TOTAL_CONTACTS_binned')
		
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=-1000.0, right_margin=1.0,
																	  closure_type=Closure(0),
																	  fix_value_output='low',
								                                      data_type_output = DataType(0),
																	  field_in = 'SELF_INIT_CNTCTS',
																	  field_out = 'SELF_INIT_CNTCTS_binned')
		
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=-1000.0, right_margin=1.0,
																	  closure_type=Closure(0),
																	  fix_value_output='low',
								                                      data_type_output = DataType(0),
																	  field_in = 'SOLICITED_CNTCTS',
																	  field_out = 'SOLICITED_CNTCTS_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1.0, right_margin=4.0,
																	  closure_type=Closure(2),
																	  fix_value_output='Moderate',
								                                      data_type_output = DataType(0),
																	  field_in = 'TOTAL_CONTACTS',
																	  field_out = 'TOTAL_CONTACTS_binned')
		
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1.0, right_margin=4.0,
																	  closure_type=Closure(2),
																	  fix_value_output='Moderate',
								                                      data_type_output = DataType(0),
																	  field_in = 'SELF_INIT_CNTCTS',
																	  field_out = 'SELF_INIT_CNTCTS_binned')
		
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1.0, right_margin=4.0,
																	  closure_type=Closure(2),
																	  fix_value_output='Moderate',
								                                      data_type_output = DataType(0),
																	  field_in = 'SOLICITED_CNTCTS',
																	  field_out = 'SOLICITED_CNTCTS_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=4.0, right_margin=1000.0,
																	  closure_type=Closure(2),
																	  fix_value_output='High',
								                                      data_type_output = DataType(0),
																	  field_in = 'TOTAL_CONTACTS',
																	  field_out = 'TOTAL_CONTACTS_binned')
		
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=4.0, right_margin=1000.0,
																	  closure_type=Closure(2),
																	  fix_value_output='High',
								                                      data_type_output = DataType(0),
																	  field_in = 'SELF_INIT_CNTCTS',
																	  field_out = 'SELF_INIT_CNTCTS_binned')
		
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=4.0, right_margin=1000.0,
																	  closure_type=Closure(2),
																	  fix_value_output='High',
								                                      data_type_output = DataType(0),
																	  field_in = 'SOLICITED_CNTCTS',
																	  field_out = 'SOLICITED_CNTCTS_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		binner_input_dataDictionary_transformed=data_dictionary.copy()
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																	  data_type_output = DataType(0),
																	  field_in = 'TERRITORY', field_out = 'TERRITORY_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=-1000.0, right_margin=1.0,
																	  closure_type=Closure(0),
																	  fix_value_output='Unknown',
								                                      data_type_output = DataType(0),
																	  field_in = 'TERRITORY',
																	  field_out = 'TERRITORY_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1.0, right_margin=3.0,
																	  closure_type=Closure(2),
																	  fix_value_output='Zone 1',
								                                      data_type_output = DataType(0),
																	  field_in = 'TERRITORY',
																	  field_out = 'TERRITORY_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=3.0, right_margin=5.0,
																	  closure_type=Closure(2),
																	  fix_value_output='Zone 2',
								                                      data_type_output = DataType(0),
																	  field_in = 'TERRITORY',
																	  field_out = 'TERRITORY_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=5.0, right_margin=7.0,
																	  closure_type=Closure(2),
																	  fix_value_output='Zone 3',
								                                      data_type_output = DataType(0),
																	  field_in = 'TERRITORY',
																	  field_out = 'TERRITORY_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=7.0, right_margin=1000.0,
																	  closure_type=Closure(3),
																	  fix_value_output='Zone 4',
								                                      data_type_output = DataType(0),
																	  field_in = 'TERRITORY',
																	  field_out = 'TERRITORY_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		binner_input_dataDictionary_transformed=data_dictionary.copy()
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																	  data_type_output = DataType(0),
																	  field_in = 'satscore', field_out = 'satscore_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=-1000.0, right_margin=1040.0,
																	  closure_type=Closure(1),
																	  fix_value_output='54 Percentile and Under',
								                                      data_type_output = DataType(0),
																	  field_in = 'satscore',
																	  field_out = 'satscore_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1040.0, right_margin=1160.0,
																	  closure_type=Closure(1),
																	  fix_value_output='55-75 Percentile',
								                                      data_type_output = DataType(0),
																	  field_in = 'satscore',
																	  field_out = 'satscore_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1160.0, right_margin=1340.0,
																	  closure_type=Closure(2),
																	  fix_value_output='76-93 Percentile',
								                                      data_type_output = DataType(0),
																	  field_in = 'satscore',
																	  field_out = 'satscore_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1340.0, right_margin=2000.0,
																	  closure_type=Closure(2),
																	  fix_value_output='94+ percentile',
								                                      data_type_output = DataType(0),
																	  field_in = 'satscore',
																	  field_out = 'satscore_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')
		print('NO ES MAPPING')
		binner_input_dataDictionary_transformed=data_dictionary.copy()
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																	  data_type_output = DataType(0),
																	  field_in = 'avg_income', field_out = 'avg_income_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=-1000.0, right_margin=1040.0,
																	  closure_type=Closure(1),
																	  fix_value_output='Low',
								                                      data_type_output = DataType(0),
																	  field_in = 'avg_income',
																	  field_out = 'avg_income_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1040.0, right_margin=1160.0,
																	  closure_type=Closure(1),
																	  fix_value_output='Moderate',
								                                      data_type_output = DataType(0),
																	  field_in = 'avg_income',
																	  field_out = 'avg_income_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
		print('Binner')
		binner_input_dataDictionary_transformed=transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																	  left_margin=1160.0, right_margin=1340.0,
																	  closure_type=Closure(2),
																	  fix_value_output='High',
								                                      data_type_output = DataType(0),
																	  field_in = 'avg_income',
																	  field_out = 'avg_income_binned')
		
		binner_output_dataDictionary=binner_input_dataDictionary_transformed
		binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
		
















dp=DataProcessing()
dp.generateDataProcessing()
