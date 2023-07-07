if __name__ == "__main__":
    import os
    import sys
    
    if len(sys.argv) < 3:
        print("Error: <python rename scripts> not enough arguments")
        sys.exit(1)

    _, project_name, project_path = sys.argv

    xmake_lua_path = os.path.join(project_path, "xmake.lua")

    if not os.path.exists(xmake_lua_path):
        print("Error: <python rename scripts> xmake.lua not exists")
        sys.exit(1)

    with open(xmake_lua_path, "r") as f:
        content = f.read()

    with open(xmake_lua_path, "w") as f:
        f.write(content.replace("$(ProjectName)", project_name))
