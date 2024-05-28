import os

import pandas as pd
import functions.contract_invariants as contract_invariants
import functions.contract_pre_post as contract_pre_post
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure
class DataProcessing:
	def generateDataProcessing(self):
		pre_post=contract_pre_post.ContractsPrePost()
		invariants=contract_invariants.Invariants()
#-----------------New DataProcessing-----------------
		imputeByDerivedValue_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			imputeByDerivedValue_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv', sep = ',')

		missing_values_imputeMissingByMostFrequent(sex)_PRE_value_range=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByDerivedValue_input_dataDictionary, field='sex', 
										missing_values=missing_values_imputeMissingByMostFrequent(sex)_PRE_value_range,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION imputeMissingByMostFrequent(sex)_PRE_value_range VALIDATED')
		else:
			print('PRECONDITION imputeMissingByMostFrequent(sex)_PRE_value_range NOT VALIDATED')
		
		missing_values_imputeMissingByMostFrequent(IRSCHOOL)_PRE_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByDerivedValue_input_dataDictionary, field='IRSCHOOL', 
										missing_values=missing_values_imputeMissingByMostFrequent(IRSCHOOL)_PRE_valueRange,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION imputeMissingByMostFrequent(IRSCHOOL)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeMissingByMostFrequent(IRSCHOOL)_PRE_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByMostFrequent(ETHNICITY)_PRE_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByDerivedValue_input_dataDictionary, field='ETHNICITY', 
										missing_values=missing_values_imputeMissingByMostFrequent(ETHNICITY)_PRE_valueRange,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION imputeMissingByMostFrequent(ETHNICITY)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeMissingByMostFrequent(ETHNICITY)_PRE_valueRange NOT VALIDATED')
		
		missing_values_POST_value_range_impute_sex_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByDerivedValue_output_dataDictionary, field='sex', 
										missing_values=missing_values_POST_value_range_impute_sex_columns,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_sex_columns VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_sex_columns NOT VALIDATED')
		
		missing_values_POST_value_range_impute_IRSCHOOL_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByDerivedValue_output_dataDictionary, field='IRSCHOOL', 
										missing_values=missing_values_POST_value_range_impute_IRSCHOOL_columns,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_IRSCHOOL_columns VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_IRSCHOOL_columns NOT VALIDATED')
		
		missing_values_POST_value_range_impute_ETHNICITY_columns=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByDerivedValue_output_dataDictionary, field='ETHNICITY', 
										missing_values=missing_values_POST_value_range_impute_ETHNICITY_columns,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION POST_value_range_impute_ETHNICITY_columns VALIDATED')
		else:
			print('POSTCONDITION POST_value_range_impute_ETHNICITY_columns NOT VALIDATED')
		
		missing_values_INV_condition_impute_sex_columns=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=imputeByDerivedValue_input_dataDictionary,
									data_dictionary_out=imputeByDerivedValue_output_dataDictionary,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_sex_columns, axis_param=0, field='sex'):
			print('INVARIANT INV_condition_impute_sex_columns VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_sex_columns NOT VALIDATED')
		
		
		missing_values_INV_condition_impute_IRSCHOOL_columns=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=imputeByDerivedValue_input_dataDictionary,
									data_dictionary_out=imputeByDerivedValue_output_dataDictionary,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_IRSCHOOL_columns, axis_param=0, field='IRSCHOOL'):
			print('INVARIANT INV_condition_impute_IRSCHOOL_columns VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_IRSCHOOL_columns NOT VALIDATED')
		
		
		missing_values_INV_condition_impute_ETHNICITY_columns=[]
		if invariants.check_inv_special_value_derived_value(data_dictionary_in=imputeByDerivedValue_input_dataDictionary,
									data_dictionary_out=imputeByDerivedValue_output_dataDictionary,
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									special_type_input=SpecialType(0),
									derived_type_output=DerivedType(0),
									missing_values=missing_values_INV_condition_impute_ETHNICITY_columns, axis_param=0, field='ETHNICITY'):
			print('INVARIANT INV_condition_impute_ETHNICITY_columns VALIDATED')
		else:
			print('INVARIANT INV_condition_impute_ETHNICITY_columns NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		imputeByFixValue_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			imputeByFixValue_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv', sep = ',')

		missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_2)_PRE_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByFixValue_input_dataDictionary, field='ACADEMIC_INTEREST_2', 
										missing_values=missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_2)_PRE_valueRange,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_PRE_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_1)_PRE_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByFixValue_input_dataDictionary, field='ACADEMIC_INTEREST_1', 
										missing_values=missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_1)_PRE_valueRange,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_PRE_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_2)_POST_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByFixValue_output_dataDictionary, field='ACADEMIC_INTEREST_2', 
										missing_values=missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_2)_POST_valueRange,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_POST_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_1)_POST_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByFixValue_output_dataDictionary, field='ACADEMIC_INTEREST_1', 
										missing_values=missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_1)_POST_valueRange,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_POST_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_2)_INV_condition=[]
		if invariants.check_inv_special_value_fix_value(data_dictionary_in=imputeByFixValue_input_dataDictionary,
									data_dictionary_out=imputeByFixValue_output_dataDictionary,
									special_type_input=SpecialType(0),
									fix_value_output='Unknown',
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									data_type_output=DataType(0),
									missing_values=missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_2)_INV_condition, 
									axis_param=0, field='ACADEMIC_INTEREST_2'):
			print('INVARIANT imputeMissingByFixValue(ACADEMIC_INTEREST_2)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeMissingByFixValue(ACADEMIC_INTEREST_2)_INV_condition NOT VALIDATED')
		
		
		missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_1)_INV_condition=[]
		if invariants.check_inv_special_value_fix_value(data_dictionary_in=imputeByFixValue_input_dataDictionary,
									data_dictionary_out=imputeByFixValue_output_dataDictionary,
									special_type_input=SpecialType(0),
									fix_value_output='Unknown',
									belong_op_in=Belong(0),
									belong_op_out=Belong(0),
									data_type_output=DataType(0),
									missing_values=missing_values_imputeMissingByFixValue(ACADEMIC_INTEREST_1)_INV_condition, 
									axis_param=0, field='ACADEMIC_INTEREST_1'):
			print('INVARIANT imputeMissingByFixValue(ACADEMIC_INTEREST_1)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeMissingByFixValue(ACADEMIC_INTEREST_1)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			imputeByNumericOp_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv', sep = ',')

		missing_values_imputeMissingByMean(avg_income)_PRE_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByNumericOp_input_dataDictionary, field='avg_income', 
										missing_values=missing_values_imputeMissingByMean(avg_income)_PRE_valueRange,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION imputeMissingByMean(avg_income)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeMissingByMean(avg_income)_PRE_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByMean(distance)_PRE_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByNumericOp_input_dataDictionary, field='distance', 
										missing_values=missing_values_imputeMissingByMean(distance)_PRE_valueRange,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION imputeMissingByMean(distance)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeMissingByMean(distance)_PRE_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByMean(avg_income)_POST_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByNumericOp_output_dataDictionary, field='avg_income', 
										missing_values=missing_values_imputeMissingByMean(avg_income)_POST_valueRange,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeMissingByMean(avg_income)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION imputeMissingByMean(avg_income)_POST_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByMean(distance)_POST_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByNumericOp_output_dataDictionary, field='distance', 
										missing_values=missing_values_imputeMissingByMean(distance)_POST_valueRange,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeMissingByMean(distance)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION imputeMissingByMean(distance)_POST_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByMean(avg_income)_INV_condition=[]
		if invariants.check_inv_special_value_num_op(data_dictionary_in=imputeByNumericOp_input_dataDictionary,
												data_dictionary_out=imputeByNumericOp_output_dataDictionary,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(0),
												num_op_output=Operation(1),
												missing_values=missing_values_imputeMissingByMean(avg_income)_INV_condition, axis_param=0, field='avg_income'):
			print('INVARIANT imputeMissingByMean(avg_income)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeMissingByMean(avg_income)_INV_condition NOT VALIDATED')
		
		
		missing_values_imputeMissingByMean(distance)_INV_condition=[]
		if invariants.check_inv_special_value_num_op(data_dictionary_in=imputeByNumericOp_input_dataDictionary,
												data_dictionary_out=imputeByNumericOp_output_dataDictionary,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(0),
												num_op_output=Operation(1),
												missing_values=missing_values_imputeMissingByMean(distance)_INV_condition, axis_param=0, field='distance'):
			print('INVARIANT imputeMissingByMean(distance)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeMissingByMean(distance)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByMean(avg_income, distance)_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			imputeByNumericOp_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv', sep = ',')

		missing_values_imputeMissingByLinearInterpolation(satscore)_PRE_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeByNumericOp_input_dataDictionary, field='satscore', 
										missing_values=missing_values_imputeMissingByLinearInterpolation(satscore)_PRE_valueRange,
										quant_op=Operator(3), quant_rel=60.0/100):
			print('PRECONDITION imputeMissingByLinearInterpolation(satscore)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeMissingByLinearInterpolation(satscore)_PRE_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByLinearInterpolation(satscore)_POST_valueRange=[]
		if pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeByNumericOp_output_dataDictionary, field='satscore', 
										missing_values=missing_values_imputeMissingByLinearInterpolation(satscore)_POST_valueRange,
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeMissingByLinearInterpolation(satscore)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION imputeMissingByLinearInterpolation(satscore)_POST_valueRange NOT VALIDATED')
		
		missing_values_imputeMissingByLinearInterpolation(satscore)_INV_condition=[]
		if invariants.check_inv_special_value_num_op(data_dictionary_in=imputeByNumericOp_input_dataDictionary,
												data_dictionary_out=imputeByNumericOp_output_dataDictionary,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(0),
												num_op_output=Operation(0),
												missing_values=missing_values_imputeMissingByLinearInterpolation(satscore)_INV_condition, axis_param=0, field='satscore'):
			print('INVARIANT imputeMissingByLinearInterpolation(satscore)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeMissingByLinearInterpolation(satscore)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		rowFilter_input_DataDictionary=pd.read_csv('./knime_dataDictionaries/imputeMissingByLinearInterpolation(satscore)_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			rowFilter_output_DataDictionary=pd.read_csv('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',')

		if pre_post.check_fix_value_range(value=0, data_dictionary=rowFilter_input_DataDictionary, belong_op=Belong(0), field='init_span',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION rowFilter(init_span)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION rowFilter(init_span)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_fix_value_range(value='0', data_dictionary=rowFilter_output_DataDictionary, belong_op=Belong(1), field='init_span',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION rowFilter(init_span)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION rowFilter(init_span)_POST_valueRange NOT VALIDATED')
		
#-----------------New DataProcessing-----------------
		columnFilter_input_DataDictionary=pd.read_csv('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			columnFilter_output_DataDictionary=pd.read_csv('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',')

		field_list_columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_PRE_fieldRange=['TRAVEL_INIT_CNTCTS', 'REFERRAL_CNCTS', 'telecq', 'stuemail', 'interest']
		if pre_post.check_field_range(fields=field_list_columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_PRE_fieldRange,
									data_dictionary=columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_input_dataField,
									belong_op=Belong(0)):
			print('PRECONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_PRE_fieldRange VALIDATED')
		else:
			print('PRECONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_PRE_fieldRange NOT VALIDATED')
		
		
		field_list_columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_POST_fieldRange=['stuemail', 'interest', 'telecq', 'TRAVEL_INIT_CNTCTS', 'REFERRAL_CNCTS']
		if pre_post.check_field_range(fields=field_list_columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_POST_fieldRange,
									data_dictionary=data_model_column_cont_filter_out,
									belong_op=Belong(1)):
			print('POSTCONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_POST_fieldRange VALIDATED')
		else:
			print('POSTCONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_POST_fieldRange NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		mapping_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			mapping_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',')

		if pre_post.check_fix_value_range(value='A', data_dictionary=mapping_input_dataDictionary, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION mapping(TERRITORY)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION mapping(TERRITORY)_PRE_valueRange NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=mapping_input_dataDictionary, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION mapping(TERRITORY)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION mapping(TERRITORY)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_fix_value_range(value='A', data_dictionary=mapping_output_dataDictionary, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION mapping(TERRITORY)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION mapping(TERRITORY)_POST_valueRange NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=mapping_output_dataDictionary, belong_op=Belong(0), field='TERRITORY',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION mapping(TERRITORY)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION mapping(TERRITORY)_POST_valueRange NOT VALIDATED')
		
		
		input_values_list_Mapping(TERRITORY)_INV_condition=['A', 'N']
		output_values_list_Mapping(TERRITORY)_INV_condition=['0', '0']
		
		data_type_input_list_Mapping(TERRITORY)_INV_condition=[DataType(0), DataType(0)]
		data_type_output_list_Mapping(TERRITORY)_INV_condition=[DataType(0), DataType(0)]
		
		if invariants.check_inv_fix_value_fix_value(data_dictionary_in=mapping_input_dataDictionary,
												data_dictionary_out=mapping_output_dataDictionary,
												input_values_list=input_values_list_Mapping(TERRITORY)_INV_condition, 
												output_values_list=output_values_list_Mapping(TERRITORY)_INV_condition,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												data_type_input_list=data_type_input_list_Mapping(TERRITORY)_INV_condition,
												data_type_output_list=data_type_output_list_Mapping(TERRITORY)_INV_condition,
												field='TERRITORY'):
			print('INVARIANT Mapping(TERRITORY)_INV_condition VALIDATED')
		else:
			print('INVARIANT Mapping(TERRITORY)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		mapping_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			mapping_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',')

		if pre_post.check_fix_value_range(value='Y', data_dictionary=mapping_input_dataDictionary, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION mapping(Instate)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION mapping(Instate)_PRE_valueRange NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=mapping_input_dataDictionary, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION mapping(Instate)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION mapping(Instate)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_fix_value_range(value='Y', data_dictionary=mapping_output_dataDictionary, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION mapping(Instate)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION mapping(Instate)_POST_valueRange NOT VALIDATED')
		if pre_post.check_fix_value_range(value='N', data_dictionary=mapping_output_dataDictionary, belong_op=Belong(0), field='Instate',
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION mapping(Instate)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION mapping(Instate)_POST_valueRange NOT VALIDATED')
		
		
		input_values_list_mapping(Instate)_INV_condition=['Y', 'N']
		output_values_list_mapping(Instate)_INV_condition=['1', '0']
		
		data_type_input_list_mapping(Instate)_INV_condition=[DataType(0), DataType(0)]
		data_type_output_list_mapping(Instate)_INV_condition=[DataType(0), DataType(0)]
		
		if invariants.check_inv_fix_value_fix_value(data_dictionary_in=mapping_input_dataDictionary,
												data_dictionary_out=mapping_output_dataDictionary,
												input_values_list=input_values_list_mapping(Instate)_INV_condition, 
												output_values_list=output_values_list_mapping(Instate)_INV_condition,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												data_type_input_list=data_type_input_list_mapping(Instate)_INV_condition,
												data_type_output_list=data_type_output_list_mapping(Instate)_INV_condition,
												field='Instate'):
			print('INVARIANT mapping(Instate)_INV_condition VALIDATED')
		else:
			print('INVARIANT mapping(Instate)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		categoricalToContinuous_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			categoricalToContinuous_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',')

		if invariants.check_inv_missing_value_missing_value(data_dictionary_in=categoricalToContinuous_input_dataDictionary,
												data_dictionary_out=categoricalToContinuous_output_dataDictionary,
												belong_op_out=Belong(1), field='TERRITORY'):
			print('INVARIANT INV_condition_TERRITORY VALIDATED')
		else:
			print('INVARIANT INV_condition_TERRITORY NOT VALIDATED')
		
		
		if invariants.check_inv_missing_value_missing_value(data_dictionary_in=categoricalToContinuous_input_dataDictionary,
												data_dictionary_out=categoricalToContinuous_output_dataDictionary,
												belong_op_out=Belong(1), field='Instate'):
			print('INVARIANT INV_condition_Instate VALIDATED')
		else:
			print('INVARIANT INV_condition_Instate NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		imputeByNumericOp_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			imputeByNumericOp_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')

		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=imputeByNumericOp_input_dataDictionary, field='avg_income', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION imputeOutlierByClosest(avg_income)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeOutlierByClosest(avg_income)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=imputeByNumericOp_input_dataDictionary, field='distance', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION imputeOutlierByClosest(distance)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeOutlierByClosest(distance)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(0), data_dictionary=imputeByNumericOp_input_dataDictionary, field='Instate', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('PRECONDITION imputeOutlierByClosest(Instate)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION imputeOutlierByClosest(Instate)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=imputeByNumericOp_output_dataDictionary, field='avg_income', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeOutlierByClosest(avg_income)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION imputeOutlierByClosest(avg_income)_POST_valueRange NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=imputeByNumericOp_output_dataDictionary, field='distance', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeOutlierByClosest(distance)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION imputeOutlierByClosest(distance)_POST_valueRange NOT VALIDATED')
		
		if pre_post.check_outliers(belong_op=Belong(1), data_dictionary=imputeByNumericOp_output_dataDictionary, field='Instate', 
										quant_abs=None, quant_rel=None, quant_op=None):
			print('POSTCONDITION imputeOutlierByClosest(Instate)_POST_valueRange´ VALIDATED')
		else:
			print('POSTCONDITION imputeOutlierByClosest(Instate)_POST_valueRange´ NOT VALIDATED')
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=imputeByNumericOp_input_dataDictionary,
												data_dictionary_out=imputeByNumericOp_output_dataDictionary,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='avg_income'):
			print('INVARIANT imputeOutlierByClosest(avg_income)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeOutlierByClosest(avg_income)_INV_condition NOT VALIDATED')
		
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=imputeByNumericOp_input_dataDictionary,
												data_dictionary_out=imputeByNumericOp_output_dataDictionary,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='distance'):
			print('INVARIANT imputeOutlierByClosest(distance)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeOutlierByClosest(distance)_INV_condition NOT VALIDATED')
		
		
		if invariants.check_inv_special_value_num_op(data_dictionary_in=imputeByNumericOp_input_dataDictionary,
												data_dictionary_out=imputeByNumericOp_output_dataDictionary,
												belong_op_in=Belong(0),
												belong_op_out=Belong(0),
												special_type_input=SpecialType(2),
												num_op_output=Operation(3),
												missing_values=None, axis_param=0, field='Instate'):
			print('INVARIANT imputeOutlierByClosest(Instate)_INV_condition VALIDATED')
		else:
			print('INVARIANT imputeOutlierByClosest(Instate)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			binner_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=binner_input_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(0), field='TOTAL_CONTACTS'):
			print('PRECONDITION binner(TOTAL_CONTACTS)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION binner(TOTAL_CONTACTS)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=binner_input_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(0), field='SELF_INIT_CNTCTS'):
			print('PRECONDITION binner(SELF_INIT_CNTCTS)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION binner(SELF_INIT_CNTCTS)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=binner_input_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(0), field='SOLICITED_CNTCTS'):
			print('PRECONDITION binner(SOLICITED_CNTCTS)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION binner(SOLICITED_CNTCTS)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=binner_output_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='TOTAL_CONTACTS_binned'):
			print('POSTCONDITION binner(TOTAL_CONTACTS)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION binner(TOTAL_CONTACTS)_POST_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=binner_output_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='SELF_INIT_CNTCTS_binned'):
			print('POSTCONDITION binner(SELF_INIT_CNTCTS)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION binner(SELF_INIT_CNTCTS)_POST_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1.0, data_dictionary=binner_input_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='SOLICITED_CNTCTS'):
			print('POSTCONDITION binner(SOLICITED_CNTCTS)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION binner(SOLICITED_CNTCTS)_POST_valueRange NOT VALIDATED')
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Low',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TOTAL_CONTACTS'):
			print('INVARIANT binner(TOTAL_CONTACTS)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TOTAL_CONTACTS)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=1.0, right_margin=4.0,
												closure_type=Closure(2),
												fix_value_output='Moderate',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TOTAL_CONTACTS'):
			print('INVARIANT binner(TOTAL_CONTACTS)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TOTAL_CONTACTS)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=4.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='High',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TOTAL_CONTACTS'):
			print('INVARIANT binner(TOTAL_CONTACTS)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TOTAL_CONTACTS)_INV_condition NOT VALIDATED')
		
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Low',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SELF_INIT_CNTCTS'):
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=1.0, right_margin=4.0,
												closure_type=Closure(2),
												fix_value_output='Moderate',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SELF_INIT_CNTCTS'):
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=4.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='High',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SELF_INIT_CNTCTS'):
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS VALIDATED')
		else:
			print('INVARIANT INV_binner_condition_SELF_INIT_CNTCTS NOT VALIDATED')
		
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Low',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SOLICITED_CNTCTS'):
			print('INVARIANT binner(SOLICITED_CNTCTS)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(SOLICITED_CNTCTS)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=1.0, right_margin=4.0,
												closure_type=Closure(2),
												fix_value_output='Moderate',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SOLICITED_CNTCTS'):
			print('INVARIANT binner(SOLICITED_CNTCTS)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(SOLICITED_CNTCTS)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=4.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='High',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='SOLICITED_CNTCTS'):
			print('INVARIANT binner(SOLICITED_CNTCTS)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(SOLICITED_CNTCTS)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			binner_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

		if pre_post.check_interval_range_float(left_margin=0.0, right_margin=1000.0, data_dictionary=binner_input_dataDictionary,
		                                	closure_type=Closure(3), belong_op=Belong(0), field='TERRITORY'):
			print('PRECONDITION binner(TERRITORY)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION binner(TERRITORY)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=0.0, right_margin=1000.0, data_dictionary=binner_output_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='TERRITORY_binned'):
			print('POSTCONDITION binner(TERRITORY)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION binner(TERRITORY)_POST_valueRange NOT VALIDATED')
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=-1000.0, right_margin=1.0,
												closure_type=Closure(0),
												fix_value_output='Unknown',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT binner(TERRITORY)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TERRITORY)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=1.0, right_margin=3.0,
												closure_type=Closure(2),
												fix_value_output='Zone 1',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT binner(TERRITORY)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TERRITORY)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=3.0, right_margin=5.0,
												closure_type=Closure(2),
												fix_value_output='Zone 2',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT binner(TERRITORY)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TERRITORY)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=5.0, right_margin=7.0,
												closure_type=Closure(2),
												fix_value_output='Zone 3',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT binner(TERRITORY)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TERRITORY)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=7.0, right_margin=1000.0,
												closure_type=Closure(2),
												fix_value_output='Zone 4',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='TERRITORY'):
			print('INVARIANT binner(TERRITORY)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(TERRITORY)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			binner_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=2000.0, data_dictionary=binner_input_dataDictionary,
		                                	closure_type=Closure(3), belong_op=Belong(0), field='satscore'):
			print('PRECONDITION binner(satscore)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION binner(satscore)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=2000.0, data_dictionary=binner_output_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='satscore_binned'):
			print('POSTCONDITION binner(satscore)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION binner(satscore)_POST_valueRange NOT VALIDATED')
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=-1000.0, right_margin=1040.0,
												closure_type=Closure(1),
												fix_value_output='54 Percentile and Under',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='satscore'):
			print('INVARIANT binner(satscore)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(satscore)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=1040.0, right_margin=1160.0,
												closure_type=Closure(1),
												fix_value_output='55-75 Percentile',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='satscore'):
			print('INVARIANT binner(satscore)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(satscore)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=1160.0, right_margin=1340.0,
												closure_type=Closure(2),
												fix_value_output='76-93 Percentile',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='satscore'):
			print('INVARIANT binner(satscore)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(satscore)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=1340.0, right_margin=2000.0,
												closure_type=Closure(2),
												fix_value_output='94+ percentile',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='satscore'):
			print('INVARIANT binner(satscore)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(satscore)_INV_condition NOT VALIDATED')
		
		
#-----------------New DataProcessing-----------------
		binner_input_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')
		if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
			binner_output_dataDictionary=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

		if pre_post.check_interval_range_float(left_margin=9.0, right_margin=100000.0, data_dictionary=binner_input_dataDictionary,
		                                	closure_type=Closure(3), belong_op=Belong(0), field='avg_income'):
			print('PRECONDITION binner(avg_income)_PRE_valueRange VALIDATED')
		else:
			print('PRECONDITION binner(avg_income)_PRE_valueRange NOT VALIDATED')
		
		if pre_post.check_interval_range_float(left_margin=9.0, right_margin=100000.0, data_dictionary=binner_output_dataDictionary,
		                                	closure_type=Closure(0), belong_op=Belong(1), field='avg_income_binned'):
			print('POSTCONDITION binner(avg_income)_POST_valueRange VALIDATED')
		else:
			print('POSTCONDITION binner(avg_income)_POST_valueRange NOT VALIDATED')
		
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=9.0, right_margin=42830.0,
												closure_type=Closure(0),
												fix_value_output='Low',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='avg_income'):
			print('INVARIANT binner(avg_income)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(avg_income)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=42830.0, right_margin=5559.0,
												closure_type=Closure(2),
												fix_value_output='Moderate',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='avg_income'):
			print('INVARIANT binner(avg_income)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(avg_income)_INV_condition NOT VALIDATED')
		if invariants.check_inv_interval_fix_value(data_dictionary_in=binner_input_dataDictionary,
												data_dictionary_out=binner_output_dataDictionary,
												left_margin=5559.0, right_margin=100000.0,
												closure_type=Closure(2),
												fix_value_output='High',
												belong_op_in=Belong(0), belong_op_out=Belong(0),
												data_type_output=DataType(0),
												field='avg_income'):
			print('INVARIANT binner(avg_income)_INV_condition VALIDATED')
		else:
			print('INVARIANT binner(avg_income)_INV_condition NOT VALIDATED')
		
		
















dp=DataProcessing()
dp.generateDataProcessing()
