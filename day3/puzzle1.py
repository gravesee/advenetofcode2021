import pandas as pd

def bits_to_decimal(bits):
  out = 0
  for bit in bits:
      out = (out << 1) | bit
  return out

with open('test.txt', 'r') as fin:
  bits = map(lambda x: list(x.strip()), fin.readlines())
  df = pd.DataFrame(bits, dtype=float)
  
  gamma = (df.mean(axis=0) > 0.5).astype(int)
  epsilon = 1 - gamma  

  gam_dec = bits_to_decimal(gamma)
  eps_dec = bits_to_decimal(epsilon)

  print(gam_dec * eps_dec)

  # oxygen and co2
  
  tmp = df.copy()
  for i in range(df.shape[1]):
    oxy_filter = tmp.mean(axis=0) > 0.5
    cols = (tmp == oxy_filter)
    # print(i)
    tmp = tmp.loc[cols.loc[:,i]]
    # print(tmp.shape)
    if (tmp.shape[0] == 1):
      break
  oxy_value = bits_to_decimal(tmp.iloc[0,:].astype(int).to_list())

  
  co2_filter = df.mean(axis=0) < 0.5
  print(df.sum(axis=0), df.shape)
  cols = (df == co2_filter)

  tmp = df.copy()
  for i in cols.columns:
    tmp = tmp.loc[cols.loc[:,i]]
    # print(tmp.shape)
    if (tmp.shape[0] == 1):
      break
  co2_value = bits_to_decimal(tmp.iloc[0,:].astype(int).to_list())

  print(oxy_value, co2_value)
  
  print(oxy_value * co2_value)
  




