


def generateTable(num) :
    table = ""
    for i in range(1,11) :
        table += f"{i} X {num} = {i*num}\n"

    with open(f"tables/table_{num}","w") as f : 
        f.write(table)

for i in range(2,21) :
    generateTable(i)