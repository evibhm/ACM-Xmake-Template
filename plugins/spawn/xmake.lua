task("spawn")
    set_category("plugin")

    on_run(function (target) 
        -- local name = target:name()
        -- print(name)
        import("core.base.option")
        local pnames = option.get("pnames")

        if pnames then
            for _, pname in ipairs(pnames) do
                local template_path = path.join("$(projectdir)", "template")
                if not os.exists(template_path) then
                    print("The template project is not found!")
                    return
                end
                local project_path = path.join("$(projectdir)", pname)
                if os.exists(project_path) then
                    print("The project is already exists!")
                    return
                end
                
                os.cp(template_path, project_path)

                local script_path = path.join("$(scriptdir)", "rename.py")
                os.exec("python %s %s %s", script_path, pname, project_path)

                print("Project %s is created successfully!", pname)
            end
        else
            print("Please input at least one project name!")
        end
    end)

    set_menu {
        usage = "xmake spawn [options]",
        description = "Create new projects by the template projects.",
        options = {
            {nil, "pnames", "vs", nil, "The Project Names." }
        }
    } 