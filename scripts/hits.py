import math

mat = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

mat_trans = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0]
]

hub_vec = [1, 1, 1, 1]
auth_vec = [1, 1, 1, 1]


def normalize(data):
    sum_data = 0
    for d in data:
        sum_data += d ** 2

    for i in range(len(data)):
        data[i] = data[i] / math.sqrt(sum_data)

    return data

for k in range(3):
    # Calculate auth score
    for i, col in enumerate(mat_trans):
        sum_auth = 0
        for j in range(len(auth_vec)):
            sum_auth += col[j] * hub_vec[j]

        auth_vec[i] = sum_auth

    # Calculate hub score
    for i, col in enumerate(mat):
        sum_hub = 0
        for j in range(len(hub_vec)):
            sum_hub += col[j] * auth_vec[j]

        hub_vec[i] = sum_hub
    #print("Iteration:", k, " , hub: ", hub_vec)


            
    #print("Iteration:", k, " , auth: ", auth_vec)
    hub_vec = normalize(hub_vec)
    auth_vec = normalize(auth_vec)

    print("-------------- Iteration", k, " --------------")
    print("Normalized authority score:")
    print("\tA: ", auth_vec[0]) 
    print("\tB: ", auth_vec[1]) 
    print("\tC: ", auth_vec[2]) 
    print("\tD: ", auth_vec[3]) 

    print()

    print("Normalized hub score:")
    print("\tA: ", hub_vec[0]) 
    print("\tB: ", hub_vec[1]) 
    print("\tC: ", hub_vec[2]) 
    print("\tD: ", hub_vec[3]) 

    print("\n")


