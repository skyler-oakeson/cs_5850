# A02308556, Skyler Oakeson, skyler.oakeson@gmail.com, Assignment 1
import numpy as np
import pandas as pd
from openai import OpenAI
from gensim.models import word2vec
from gensim.models import KeyedVectors
from numpy.linalg import norm


client = OpenAI(api_key=my_api_key)

toast = client.embeddings.create(
        input="toast",
        model="text-embedding-3-small"
)

breakfast = client.embeddings.create(
        input="breakfast",
        model="text-embedding-3-small"
)

dinner = client.embeddings.create(
        input="dinner",
        model="text-embedding-3-small"
)

e_toast = np.array(toast.data[0].embedding)
e_breakfast = np.array(breakfast.data[0].embedding)
e_dinner = np.array(dinner.data[0].embedding)

c_t_b = np.dot(e_toast, e_breakfast) / (norm(e_toast) * norm(e_breakfast))
c_t_d = np.dot(e_toast, e_dinner) / (norm(e_toast) * norm(e_dinner))

print(c_t_b)
print(c_t_d)

