import pandas as pd
import numpy as np
import functions.data_transformations as data_transformations
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType
from helpers.logger import set_logger

def generateWorkflow():
	#-----------------New DataProcessing-----------------
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/missing_input_dataDictionary.csv', sep = ',')
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df.to_csv('/wf_validation_python/data/missing_input_dataDictionary.csv')
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/missing_input_dataDictionary.csv', sep = ',')
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df.to_csv('/wf_validation_python/data/missing_input_dataDictionary.csv')
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df.copy()
	missing_values_list=[]
	
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed=data_transformations.transform_special_value_derived_value(data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'sex', field_out = 'sex')
	
	missing_values_list=[]
	
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed=data_transformations.transform_special_value_derived_value(data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'IRSCHOOL', field_out = 'IRSCHOOL')
	
	missing_values_list=[]
	
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed=data_transformations.transform_special_value_derived_value(data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), derived_type_output=DerivedType(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'ETHNICITY', field_out = 'ETHNICITY')
	
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_transformed
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df.to_csv('/wf_validation_python/data/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv')
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv', sep = ',', index_col=0)
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df.to_csv('/wf_validation_python/data/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv')
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/missing_input_dataDictionary.csv', sep=',', index_col=0)
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/missing_input_dataDictionary.csv', sep=',', index_col=0)

	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_transformed=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_df.copy()
	missing_values_list=[]
	
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_transformed=data_transformations.transform_special_value_fix_value(data_dictionary=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), fix_value_output='Unknown',
																  missing_values=missing_values_list,		
							                                      data_type_output = DataType(0),
																  axis_param=0, field_in = 'ACADEMIC_INTEREST_2', field_out = 'ACADEMIC_INTEREST_2')
	
	missing_values_list=[]
	
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_transformed=data_transformations.transform_special_value_fix_value(data_dictionary=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), fix_value_output='Unknown',
																  missing_values=missing_values_list,		
							                                      data_type_output = DataType(0),
																  axis_param=0, field_in = 'ACADEMIC_INTEREST_1', field_out = 'ACADEMIC_INTEREST_1')
	
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_transformed
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df.to_csv('/wf_validation_python/data/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv')
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv', sep = ',', index_col=0)
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df.to_csv('/wf_validation_python/data/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv')
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	imputeMissingByMean_avg_income_distance__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/missing_input_dataDictionary.csv', sep=',', index_col=0)
	imputeMissingByMean_avg_income_distance__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/missing_input_dataDictionary.csv', sep=',', index_col=0)

	imputeMissingByMean_avg_income_distance__input_dataDictionary_transformed=imputeMissingByMean_avg_income_distance__input_dataDictionary_df.copy()
	missing_values_list=[]
	
	imputeMissingByMean_avg_income_distance__input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeMissingByMean_avg_income_distance__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), num_op_output=Operation(1),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'avg_income', field_out = 'avg_income')
	
	missing_values_list=[]
	
	imputeMissingByMean_avg_income_distance__input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeMissingByMean_avg_income_distance__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), num_op_output=Operation(1),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'distance', field_out = 'distance')
	
	imputeMissingByMean_avg_income_distance__output_dataDictionary_df=imputeMissingByMean_avg_income_distance__input_dataDictionary_transformed
	imputeMissingByMean_avg_income_distance__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv')
	imputeMissingByMean_avg_income_distance__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv', sep = ',', index_col=0)
	imputeMissingByMean_avg_income_distance__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv')
	imputeMissingByMean_avg_income_distance__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	imputeMissingByLinearInterpolation_satscore__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/missing_input_dataDictionary.csv', sep=',', index_col=0)
	imputeMissingByLinearInterpolation_satscore__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/missing_input_dataDictionary.csv', sep=',', index_col=0)

	imputeMissingByLinearInterpolation_satscore__input_dataDictionary_transformed=imputeMissingByLinearInterpolation_satscore__input_dataDictionary_df.copy()
	missing_values_list=[]
	
	imputeMissingByLinearInterpolation_satscore__input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeMissingByLinearInterpolation_satscore__input_dataDictionary_transformed,
																  special_type_input=SpecialType(0), num_op_output=Operation(0),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'satscore', field_out = 'satscore')
	
	imputeMissingByLinearInterpolation_satscore__output_dataDictionary_df=imputeMissingByLinearInterpolation_satscore__input_dataDictionary_transformed
	imputeMissingByLinearInterpolation_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv')
	imputeMissingByLinearInterpolation_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv', sep = ',', index_col=0)
	imputeMissingByLinearInterpolation_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv')
	imputeMissingByLinearInterpolation_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	rowFilterRange_init_span__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/missing_output_dataDictionary.csv', sep=',', index_col=0)
	rowFilterRange_init_span__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/missing_output_dataDictionary.csv', sep=',', index_col=0)

	rowFilterRange_init_span__input_dataDictionary_transformed=rowFilterRange_init_span__input_dataDictionary_df.copy()
	columns_rowFilterRange_param_filter=['init_span']
	
	filter_range_left_values_list_rowFilterRange_param_filter=[-np.inf]
	filter_range_right_values_list_rowFilterRange_param_filter=[0.0]
	closure_type_list_rowFilterRange_param_filter=[Closure(3)]
	
	rowFilterRange_init_span__input_dataDictionary_transformed=data_transformations.transform_filter_rows_range(data_dictionary=rowFilterRange_init_span__input_dataDictionary_transformed,
																											columns=columns_rowFilterRange_param_filter,
																											left_margin_list=filter_range_left_values_list_rowFilterRange_param_filter,
																											right_margin_list=filter_range_right_values_list_rowFilterRange_param_filter,
																											filter_type=FilterType(0),
																											closure_type_list=closure_type_list_rowFilterRange_param_filter)
	rowFilterRange_init_span__output_dataDictionary_df=rowFilterRange_init_span__input_dataDictionary_transformed
	rowFilterRange_init_span__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/rowFilter_output_dataDictionary.csv')
	rowFilterRange_init_span__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',', index_col=0)
	rowFilterRange_init_span__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/rowFilter_output_dataDictionary.csv')
	rowFilterRange_init_span__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep=',', index_col=0)
	columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep=',', index_col=0)

	columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField_transformed=columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField_df.copy()
	field_list_columnFilter_param_field=['TRAVEL_INIT_CNTCTS', 'REFERRAL_CNTCTS']
	
	columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField_transformed=data_transformations.transform_filter_columns(data_dictionary=columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField_transformed,
																	columns=field_list_columnFilter_param_field, belong_op=Belong.BELONG)
	
	data_model_column_cont_filter_out_df=columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField_transformed
	data_model_column_cont_filter_out_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/columnFilter_output_dataDictionary.csv')
	data_model_column_cont_filter_out_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',', index_col=0)
	data_model_column_cont_filter_out_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/columnFilter_output_dataDictionary.csv')
	data_model_column_cont_filter_out_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	Mapping_TERRITORY__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep=',', index_col=0)
	Mapping_TERRITORY__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep=',', index_col=0)

	input_values_list=['A', 'N']
	output_values_list=['0', '0']
	data_type_input_list=[DataType(0), DataType(0)]
	data_type_output_list=[DataType(0), DataType(0)]
	
	
	Mapping_TERRITORY__output_dataDictionary_df=data_transformations.transform_fix_value_fix_value(data_dictionary=Mapping_TERRITORY__input_dataDictionary_df, input_values_list=input_values_list,
																  output_values_list=output_values_list,
							                                      data_type_input_list = data_type_input_list,
							                                      data_type_output_list = data_type_output_list, field_in = 'TERRITORY', field_out = 'TERRITORY')
	
	Mapping_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv')
	Mapping_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',', index_col=0)
	Mapping_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv')
	Mapping_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	mapping_Instate__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep=',', index_col=0)
	mapping_Instate__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep=',', index_col=0)

	input_values_list=['Y', 'N']
	output_values_list=['1', '0']
	data_type_input_list=[DataType(0), DataType(0)]
	data_type_output_list=[DataType(0), DataType(0)]
	
	
	mapping_Instate__output_dataDictionary_df=data_transformations.transform_fix_value_fix_value(data_dictionary=mapping_Instate__input_dataDictionary_df, input_values_list=input_values_list,
																  output_values_list=output_values_list,
							                                      data_type_input_list = data_type_input_list,
							                                      data_type_output_list = data_type_output_list, field_in = 'Instate', field_out = 'Instate')
	
	mapping_Instate__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv')
	mapping_Instate__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',', index_col=0)
	mapping_Instate__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv')
	mapping_Instate__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	stringToNumber_TERRITORY_Instate__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep=',', index_col=0)
	stringToNumber_TERRITORY_Instate__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep=',', index_col=0)

	stringToNumber_TERRITORY_Instate__input_dataDictionary_transformed=stringToNumber_TERRITORY_Instate__input_dataDictionary_df.copy()
	stringToNumber_TERRITORY_Instate__input_dataDictionary_transformed=data_transformations.transform_cast_type(data_dictionary=stringToNumber_TERRITORY_Instate__input_dataDictionary_transformed,
																	data_type_output= DataType(6),
																	field='TERRITORY')
	
	stringToNumber_TERRITORY_Instate__input_dataDictionary_transformed=data_transformations.transform_cast_type(data_dictionary=stringToNumber_TERRITORY_Instate__input_dataDictionary_transformed,
																	data_type_output= DataType(6),
																	field='Instate')
	
	stringToNumber_TERRITORY_Instate__output_dataDictionary_df=stringToNumber_TERRITORY_Instate__input_dataDictionary_transformed
	stringToNumber_TERRITORY_Instate__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv')
	stringToNumber_TERRITORY_Instate__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',', index_col=0)
	stringToNumber_TERRITORY_Instate__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv')
	stringToNumber_TERRITORY_Instate__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep=',', index_col=0)
	imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep=',', index_col=0)

	imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_df.copy()
	missing_values_list=[]
	
	imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed,
																  special_type_input=SpecialType(2), num_op_output=Operation(3),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'avg_income', field_out = 'avg_income')
	
	missing_values_list=[]
	
	imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed,
																  special_type_input=SpecialType(2), num_op_output=Operation(3),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'distance', field_out = 'distance')
	
	missing_values_list=[]
	
	imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed=data_transformations.transform_special_value_num_op(data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed,
																  special_type_input=SpecialType(2), num_op_output=Operation(3),
																  missing_values=missing_values_list,		
																  axis_param=0, field_in = 'Instate', field_out = 'Instate')
	
	imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_transformed
	imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv')
	imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',', index_col=0)
	imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv')
	imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)

	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_df.copy()
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS', field_out = 'TOTAL_CONTACTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS', field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS', field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='Low',
							                                      data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS',
																  field_out = 'TOTAL_CONTACTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='Low',
							                                      data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS',
																  field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='Low',
							                                      data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS',
																  field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=4.0,
																  closure_type=Closure(2),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS',
																  field_out = 'TOTAL_CONTACTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=4.0,
																  closure_type=Closure(2),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS',
																  field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=4.0,
																  closure_type=Closure(2),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS',
																  field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=4.0, right_margin=1000.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'TOTAL_CONTACTS',
																  field_out = 'TOTAL_CONTACTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=4.0, right_margin=1000.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'SELF_INIT_CNTCTS',
																  field_out = 'SELF_INIT_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed,
																  left_margin=4.0, right_margin=1000.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'SOLICITED_CNTCTS',
																  field_out = 'SOLICITED_CNTCTS_binned')
	
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_transformed
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	binner_TERRITORY__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)
	binner_TERRITORY__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)

	binner_TERRITORY__input_dataDictionary_transformed=binner_TERRITORY__input_dataDictionary_df.copy()
	binner_TERRITORY__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_TERRITORY__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'TERRITORY', field_out = 'TERRITORY_binned')
	
	binner_TERRITORY__output_dataDictionary_df=binner_TERRITORY__input_dataDictionary_transformed
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TERRITORY__input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1.0,
																  closure_type=Closure(0),
																  fix_value_output='Unknown',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_TERRITORY__output_dataDictionary_df=binner_TERRITORY__input_dataDictionary_transformed
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TERRITORY__input_dataDictionary_transformed,
																  left_margin=1.0, right_margin=3.0,
																  closure_type=Closure(2),
																  fix_value_output='Zone 1',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_TERRITORY__output_dataDictionary_df=binner_TERRITORY__input_dataDictionary_transformed
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TERRITORY__input_dataDictionary_transformed,
																  left_margin=3.0, right_margin=5.0,
																  closure_type=Closure(2),
																  fix_value_output='Zone 2',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_TERRITORY__output_dataDictionary_df=binner_TERRITORY__input_dataDictionary_transformed
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TERRITORY__input_dataDictionary_transformed,
																  left_margin=5.0, right_margin=7.0,
																  closure_type=Closure(2),
																  fix_value_output='Zone 3',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_TERRITORY__output_dataDictionary_df=binner_TERRITORY__input_dataDictionary_transformed
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_TERRITORY__input_dataDictionary_transformed,
																  left_margin=7.0, right_margin=1000.0,
																  closure_type=Closure(3),
																  fix_value_output='Zone 4',
							                                      data_type_output = DataType(0),
																  field_in = 'TERRITORY',
																  field_out = 'TERRITORY_binned')
	
	binner_TERRITORY__output_dataDictionary_df=binner_TERRITORY__input_dataDictionary_transformed
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_TERRITORY__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_TERRITORY__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	binner_satscore__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)
	binner_satscore__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)

	binner_satscore__input_dataDictionary_transformed=binner_satscore__input_dataDictionary_df.copy()
	binner_satscore__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_satscore__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'satscore', field_out = 'satscore_binned')
	
	binner_satscore__output_dataDictionary_df=binner_satscore__input_dataDictionary_transformed
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_satscore__input_dataDictionary_transformed,
																  left_margin=-1000.0, right_margin=1040.0,
																  closure_type=Closure(1),
																  fix_value_output='54 Percentile and Under',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_satscore__output_dataDictionary_df=binner_satscore__input_dataDictionary_transformed
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_satscore__input_dataDictionary_transformed,
																  left_margin=1040.0, right_margin=1160.0,
																  closure_type=Closure(0),
																  fix_value_output='55-75 Percentile',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_satscore__output_dataDictionary_df=binner_satscore__input_dataDictionary_transformed
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_satscore__input_dataDictionary_transformed,
																  left_margin=1160.0, right_margin=1340.0,
																  closure_type=Closure(2),
																  fix_value_output='76-93 Percentile',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_satscore__output_dataDictionary_df=binner_satscore__input_dataDictionary_transformed
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_satscore__input_dataDictionary_transformed,
																  left_margin=1340.0, right_margin=2000.0,
																  closure_type=Closure(1),
																  fix_value_output='94+ percentile',
							                                      data_type_output = DataType(0),
																  field_in = 'satscore',
																  field_out = 'satscore_binned')
	
	binner_satscore__output_dataDictionary_df=binner_satscore__input_dataDictionary_transformed
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_satscore__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_satscore__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	
	#-----------------New DataProcessing-----------------
	binner_avg_income__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)
	binner_avg_income__input_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',', index_col=0)

	binner_avg_income__input_dataDictionary_transformed=binner_avg_income__input_dataDictionary_df.copy()
	binner_avg_income__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_avg_income__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'avg_income', field_out = 'avg_income_binned')
	
	binner_avg_income__output_dataDictionary_df=binner_avg_income__input_dataDictionary_transformed
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_avg_income__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_avg_income__input_dataDictionary_transformed,
																  left_margin=9.0, right_margin=42830.0,
																  closure_type=Closure(1),
																  fix_value_output='Low',
							                                      data_type_output = DataType(0),
																  field_in = 'avg_income',
																  field_out = 'avg_income_binned')
	
	binner_avg_income__output_dataDictionary_df=binner_avg_income__input_dataDictionary_transformed
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_avg_income__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_avg_income__input_dataDictionary_transformed,
																  left_margin=42830.0, right_margin=55590.0,
																  closure_type=Closure(1),
																  fix_value_output='Moderate',
							                                      data_type_output = DataType(0),
																  field_in = 'avg_income',
																  field_out = 'avg_income_binned')
	
	binner_avg_income__output_dataDictionary_df=binner_avg_income__input_dataDictionary_transformed
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_avg_income__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_avg_income__input_dataDictionary_transformed,
																  left_margin=55590.0, right_margin=100000.0,
																  closure_type=Closure(2),
																  fix_value_output='High',
							                                      data_type_output = DataType(0),
																  field_in = 'avg_income',
																  field_out = 'avg_income_binned')
	
	binner_avg_income__output_dataDictionary_df=binner_avg_income__input_dataDictionary_transformed
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	binner_avg_income__output_dataDictionary_df.to_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv')
	binner_avg_income__output_dataDictionary_df=pd.read_csv('/wf_validation_python/data/./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',', index_col=0)
	














set_logger("transformations")
generateWorkflow()
