import pandas as pd
import functions.data_transformations as data_transformations
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType
from helpers.logger import set_logger

def generateDataProcessing():
#-----------------New DataProcessing-----------------
	imputeByDerivedValue_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')
	imputeByDerivedValue_input_dataDictionary_transformed=imputeByDerivedValue_input_dataDictionary.copy()
	missing_values_list=[]
	
	imputeByDerivedValue_input_dataDictionary_transformed=data_transformations.transform_special_value_derived_value(data_dictionary=imputeByDerivedValue_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'sex', field_out = 'sex')
	
	missing_values_list=[]
	
	imputeByDerivedValue_input_dataDictionary_transformed=data_transformations.transform_special_value_derived_value(data_dictionary=imputeByDerivedValue_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'IRSCHOOL', field_out = 'IRSCHOOL')
	
	missing_values_list=[]
	
	imputeByDerivedValue_input_dataDictionary_transformed=data_transformations.transform_special_value_derived_value(data_dictionary=imputeByDerivedValue_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'ETHNICITY', field_out = 'ETHNICITY')
	
	imputeByDerivedValue_output_dataDictionary=imputeByDerivedValue_input_dataDictionary_transformed
	imputeByDerivedValue_output_dataDictionary.to_csv('./knime_dataDictionaries/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	imputeByFixValue_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv', sep=',')

	imputeByFixValue_input_dataDictionary_transformed=imputeByFixValue_input_dataDictionary.copy()
	missing_values_list=[]
	
	imputeByFixValue_input_dataDictionary_transformed=data_transformations.transform_special_value_fix_value(data_dictionary=imputeByFixValue_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), fix_value_output='Unknown',
																  missing_values=missing_values_list,		
							                                      data_type_output = DataType(0),
																  axis_param=0, field_in = 'ACADEMIC_INTEREST_2', field_out = 'ACADEMIC_INTEREST_2')
	
	missing_values_list=[]
	
	imputeByFixValue_input_dataDictionary_transformed=data_transformations.transform_special_value_fix_value(data_dictionary=imputeByFixValue_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), fix_value_output='Unknown',
																  missing_values=missing_values_list,		
							                                      data_type_output = DataType(0),
																  axis_param=0, field_in = 'ACADEMIC_INTEREST_1', field_out = 'ACADEMIC_INTEREST_1')
	
	imputeByFixValue_output_dataDictionary=imputeByFixValue_input_dataDictionary_transformed
	imputeByFixValue_output_dataDictionary.to_csv('./knime_dataDictionaries/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv', sep=',')

	imputeByNumericOp_input_dataDictionary_transformed=imputeByNumericOp_input_dataDictionary.copy()
	missing_values_list=[]
	
	imputeByNumericOp_input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeByNumericOp_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), num_op_output=Operation(1),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'avg_income', field_out = 'avg_income')
	
	missing_values_list=[]
	
	imputeByNumericOp_input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeByNumericOp_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), num_op_output=Operation(1),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'distance', field_out = 'distance')
	
	imputeByNumericOp_output_dataDictionary=imputeByNumericOp_input_dataDictionary_transformed
	imputeByNumericOp_output_dataDictionary.to_csv('./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv', sep=',')

	imputeByNumericOp_input_dataDictionary_transformed=imputeByNumericOp_input_dataDictionary.copy()
	missing_values_list=[]
	
	imputeByNumericOp_input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeByNumericOp_input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), num_op_output=Operation(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'satscore', field_out = 'satscore')
	
	imputeByNumericOp_output_dataDictionary=imputeByNumericOp_input_dataDictionary_transformed
	imputeByNumericOp_output_dataDictionary.to_csv('./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	rowFilter_input_DataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv', sep=',')

	rowFilter_input_DataDictionary_transformed=rowFilter_input_DataDictionary.copy()
	columns_rowFilter_param_filter=['init_span']
	
	filter_fix_value_list_rowFilter_param_filter=[0]
	
	rowFilter_input_DataDictionary_transformed=data_transformations.transform_filter_rows_primitive(data_dictionary=rowFilter_input_DataDictionary_transformed,
																											columns=columns_rowFilter_param_filter,
																		                                    filter_fix_value_list=filter_fix_value_list_rowFilter_param_filter,
																											filter_type=FilterType(0))
	rowFilter_output_DataDictionary=rowFilter_input_DataDictionary_transformed
	rowFilter_output_DataDictionary.to_csv('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	columnFilter_input_DataDictionary=pd.read_csv('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep=',')

	columnFilter_input_DataDictionary_transformed=columnFilter_input_DataDictionary.copy()
	field_list_columnFilter_param_field=['TRAVEL_INIT_CNTCTS', 'REFERRAL_CNCTS']
	
	columnFilter_input_DataDictionary_transformed=data_transformations.transform_filter_columns(data_dictionary=columnFilter_input_DataDictionary_transformed,
																	columns=field_list_columnFilter_param_field, belong_op=Belong.BELONG)
	
	columnFilter_output_DataDictionary=columnFilter_input_DataDictionary_transformed
	columnFilter_output_DataDictionary.to_csv('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	mapping_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep=',')

	input_values_list=['A', 'N']
	output_values_list=['0', '0']
	data_type_input_list=[DataType(0), DataType(0)]
	data_type_output_list=[DataType(0), DataType(0)]
	
	
	mapping_output_dataDictionary=data_transformations.transform_fix_value_fix_value(data_dictionary=mapping_input_dataDictionary, input_values_list=input_values_list,
																  output_values_list=output_values_list,
							                                      data_type_input_list = data_type_input_list,
							                                      data_type_output_list = data_type_output_list, field_in = 'TERRITORY', field_out = 'TERRITORY')
	
	mapping_output_dataDictionary.to_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	mapping_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep=',')

	input_values_list=['Y', 'N']
	output_values_list=['1', '0']
	data_type_input_list=[DataType(0), DataType(0)]
	data_type_output_list=[DataType(0), DataType(0)]
	
	
	mapping_output_dataDictionary=data_transformations.transform_fix_value_fix_value(data_dictionary=mapping_input_dataDictionary, input_values_list=input_values_list,
																  output_values_list=output_values_list,
							                                      data_type_input_list = data_type_input_list,
							                                      data_type_output_list = data_type_output_list, field_in = 'Instate', field_out = 'Instate')
	
	mapping_output_dataDictionary.to_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	categoricalToContinuous_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep=',')

	categoricalToContinuous_input_dataDictionary_transformed=categoricalToContinuous_input_dataDictionary.copy()
	categoricalToContinuous_input_dataDictionary_transformed=data_transformations.transform_cast_type(data_dictionary=categoricalToContinuous_input_dataDictionary_transformed,
																	data_type_output= DataType(6),
																	field='TERRITORY')
	
	categoricalToContinuous_input_dataDictionary_transformed=data_transformations.transform_cast_type(data_dictionary=categoricalToContinuous_input_dataDictionary_transformed,
																	data_type_output= DataType(6),
																	field='Instate')
	
	categoricalToContinuous_output_dataDictionary=categoricalToContinuous_input_dataDictionary_transformed
	categoricalToContinuous_output_dataDictionary.to_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep=',')

	imputeByNumericOp_input_dataDictionary_transformed=imputeByNumericOp_input_dataDictionary.copy()
	missing_values_list=[]
	
	imputeByNumericOp_input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeByNumericOp_input_dataDictionary_transformed,
																  special_type_input=SpecialType(2), num_op_output=Operation(3),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'avg_income', field_out = 'avg_income')
	
	missing_values_list=[]
	
	imputeByNumericOp_input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeByNumericOp_input_dataDictionary_transformed,
																  special_type_input=SpecialType(2), num_op_output=Operation(3),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'distance', field_out = 'distance')
	
	missing_values_list=[]
	
	imputeByNumericOp_input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeByNumericOp_input_dataDictionary_transformed,
																  special_type_input=SpecialType(2), num_op_output=Operation(3),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'Instate', field_out = 'invalid')
	
	imputeByNumericOp_output_dataDictionary=imputeByNumericOp_input_dataDictionary_transformed
	imputeByNumericOp_output_dataDictionary.to_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',')

	binner_input_dataDictionary_transformed=binner_input_dataDictionary.copy()
	binner_input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS', field_out = 'TOTAL_CONTACTS_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS', field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS', field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='low',
							                                      data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS',
																  field_out = 'TOTAL_CONTACTS_binned')
	
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='low',
							                                      data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS',
																  field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='low',
							                                      data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS',
																  field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=4.0,
																  closure_type=Closure(2),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS',
																  field_out = 'TOTAL_CONTACTS_binned')
	
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=4.0,
																  closure_type=Closure(2),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS',
																  field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=4.0,
																  closure_type=Closure(2),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS',
																  field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=4.0, right_margin=1000.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS',
																  field_out = 'TOTAL_CONTACTS_binned')
	
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=4.0, right_margin=1000.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS',
																  field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=4.0, right_margin=1000.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS',
																  field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep=',')

	binner_input_dataDictionary_transformed=binner_input_dataDictionary.copy()
	binner_input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'TERRITORY', field_out = 'TERRITORY_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='Unknown',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=3.0,
																  closure_type=Closure(2),
																  fix_value_output='Zone 1',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=3.0, right_margin=5.0,
																  closure_type=Closure(2),
																  fix_value_output='Zone 2',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=5.0, right_margin=7.0,
																  closure_type=Closure(2),
																  fix_value_output='Zone 3',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=7.0, right_margin=1000.0,
																  closure_type=Closure(3),
																  fix_value_output='Zone 4',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep=',')

	binner_input_dataDictionary_transformed=binner_input_dataDictionary.copy()
	binner_input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'satscore', field_out = 'satscore_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1040.0,
																  closure_type=Closure(1),
																  fix_value_output='54 Percentile and Under',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1040.0, right_margin=1160.0,
																  closure_type=Closure(1),
																  fix_value_output='55-75 Percentile',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1160.0, right_margin=1340.0,
																  closure_type=Closure(2),
																  fix_value_output='76-93 Percentile',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1340.0, right_margin=2000.0,
																  closure_type=Closure(2),
																  fix_value_output='94+ percentile',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	
#-----------------New DataProcessing-----------------
	binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep=',')

	binner_input_dataDictionary_transformed=binner_input_dataDictionary.copy()
	binner_input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'avg_income', field_out = 'avg_income_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1040.0,
																  closure_type=Closure(1),
																  fix_value_output='Low',
							                                      data_type_output = DataType(0),
																  field_in = 'avg_income',
																  field_out = 'avg_income_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1040.0, right_margin=1160.0,
																  closure_type=Closure(1),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'avg_income',
																  field_out = 'avg_income_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_input_dataDictionary_transformed,
																  left_margin=1160.0, right_margin=1340.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'avg_income',
																  field_out = 'avg_income_binned')
	
	binner_output_dataDictionary=binner_input_dataDictionary_transformed
	binner_output_dataDictionary.to_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	














set_logger("transformations")
generateDataProcessing()
