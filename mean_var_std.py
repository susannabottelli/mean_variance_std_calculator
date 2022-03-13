import numpy as np

list = input()

def calculate(list) :
  # error
  if len(list) != 9 :
    raise ValueError("List must contain nine numbers.")
    
    # turn list into numpy array
  np_list = np.array(list)
  print(np_list)
    # 0 1 2
    # 3 4 5
    # 6 7 8

    #mean
  mean_axis2 = ([np_list[[0,1,2]].mean(), np_list[[3,4,5]].mean(), np_list[[6,7,8]].mean()])
  mean_axis1 = ([np_list[[0,3,6]].mean(), np_list[[1,4,7]].mean(), np_list[[2,5,8]].mean()])
  mean_f = np_list.mean()
      
    #variance
  var_axis2 = ([np_list[[0,1,2]].var(), np_list[[3,4,5]].var(), np_list[[6,7,8]].var()])
  var_axis1 = ([np_list[[0,3,6]].var(), np_list[[1,4,7]].var(), np_list[[2,5,8]].var()])
  var_f = np_list.var()
    
    #standard deviation
  std_axis2 = ([np_list[[0,1,2]].std(), np_list[[3,4,5]].std(), np_list[[6,7,8]].std()])
  std_axis1 = ([np_list[[0,3,6]].std(), np_list[[1,4,7]].std(), np_list[[2,5,8]].std()])
  std_f = np_list.std()
    
    #max
  max_axis2 = ([np_list[[0,1,2]].max(), np_list[[3,4,5]].max(), np_list[[6,7,8]].max()])
  max_axis1 = ([np_list[[0,3,6]].max(), np_list[[1,4,7]].max(), np_list[[2,5,8]].max()])
  max_f = np_list.max()
    
    #min
  min_axis2 = ([np_list[[0,1,2]].min(), np_list[[3,4,5]].min(), np_list[[6,7,8]].min()])
  min_axis1 = ([np_list[[0,3,6]].min(), np_list[[1,4,7]].min(), np_list[[2,5,8]].min()])
  min_f = np_list.min()
    
    #sum
  sum_axis2 = ([np_list[[0,1,2]].sum(), np_list[[3,4,5]].sum(), np_list[[6,7,8]].sum()])
  sum_axis1 = ([np_list[[0,3,6]].sum(), np_list[[1,4,7]].sum(), np_list[[2,5,8]].sum()])
  sum_f = np_list.sum()
  
  

  return {
    'mean': [mean_axis1, mean_axis2, mean_f],
    'variance': [var_axis1, var_axis2, var_f],
    'standard deviation': [std_axis1, std_axis2, std_f],
    'max': [max_axis1, max_axis2, max_f],
    'min': [min_axis1, min_axis2, min_f],
    'sum': [sum_axis1, sum_axis2, sum_f]
    }

