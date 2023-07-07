add_rules("mode.debug", "mode.release")

target("$(ProjectName)")
    set_kind("binary")
    add_files("src/*.cpp")

    on_run(function (target) 
        -- 获取一些变量
        local name = target:name()
        local obj = target:targetfile()
        local dir = target:scriptdir()

        print("on_run: %s, %s, %s", name, obj, dir)
        os.execv("python", {"tools/run.py", obj, dir})
    end)