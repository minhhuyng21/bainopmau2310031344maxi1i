def chambai():
  INP_i1 = 1
  INP_i2 = 22
  
  from s01_dapan import lonnhat
  EXPECTED_result = lonnhat(INP_i1, INP_i2)

  try:
    from s00_bailam import lonnhat
    ACTUAL_result = lonnhat(INP_i1, INP_i2)
  except:
    ACTUAL_result = None

  chambai_r = 1 if ACTUAL_result == EXPECTED_result else 0
  return chambai_r
