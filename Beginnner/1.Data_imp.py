from sklearn.datasets import load_digits # data importing from the libary default prresent
data=load_digits(as_frame=True).frame
#online we use the fectch thing
from sklearn.datasets import fetch_california_housing
datafetch=fetch_california_housing(as_frame=True).frame # asframe is framing into tabler from
print(datafetch)

