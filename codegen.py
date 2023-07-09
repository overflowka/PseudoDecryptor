import re
import cppyy

def pseudoToCpp(file):
    with open(file, 'r') as file:
        buffer = file.read()

    matches = re.findall(r'v\d+\[0\]', buffer)
    v1 = re.findall(r'v\d+', buffer)[0]

    lines = buffer.splitlines()
    size = -1

    filtered = []
    for line in lines:
        if v1 in line:
            size += 1
            filtered.append(re.sub(r'^([ ]+)|([ ]){2,}', r'\2', line))

    matches = re.findall(r'v\d+', filtered[size])
    v2 = matches[1]

    code = "#include <iostream>\n"
    code += "typedef char _BYTE;\n\n"
    code += "int main(void)\n"
    code += "{\n"
    code += f"    int {v1}[{size}];\n"
    code += f"    int {v2} = 0;\n\n"
    for i in range(size):
        code += f"    {filtered[i]}\n"
    code += "\n"
    code += "    char buffer[1337];\n"
    code += "    buffer[0] = '\\0';\n\n"
    code += f"    for (int i = 0; i < sizeof({v1}); ++i)\n"
    code += "    {\n"
    code += f"        {filtered[size]}\n"
    code += f"        ++{v2};\n"
    code += "    }\n\n"
    code += f"    for (int i = 0; i < sizeof({v1}); ++i)\n"
    code += "    {\n"
    code += "        char temp[2];\n"
    code += f"        sprintf_s(temp, \"%c\", *((char*){v1} + i));\n"
    code += "        strcat_s(buffer, temp);\n"
    code += "    }\n\n"
    code += '    printf("%s", buffer);\n'
    code += "    return 0;\n"
    code += "}"

    with open('generated.cpp', 'w') as file:
        file.write(code)

    return code

code = pseudoToCpp('pseudocode.txt')
cppyy.cppdef(code)
cppyy.gbl.main()