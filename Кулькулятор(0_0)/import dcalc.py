import dcalc

def create_list(*args, **kwargs):
    response = []
    for idx, value in enumerate(args):
        response.append(f"Point_{idx} = {dcalc.deg_to_gms(value)}")
    for k, v in kwargs.items():
        response.append(f"{k} = {dcalc.deg_to_gms(v)}")
    return response

print(
    create_list(
        180.35888161,
        352.64332111,
        27.987988781353,
        pole=21.89617856,
        put_1=140.85706440,
    )
)