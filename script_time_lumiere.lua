commandArray = {}

jourF = false

for deviceName,deviceValue in pairs(otherdevices) do
    if (deviceName=='Jour férié') then
        if deviceValue == "On" then
            print("Jour férié")
            jourF = true
        end
    end
end

if (os.date("%A") ~= "Saturday" and os.date("%A") ~= "Sunday" and not jourF) then
    if (os.date("%H:%M") == "06:50") then
        print("il est 06:50")
        if (otherdevices["Lampe Chambre"] == "Off") then
            commandArray["Lampe Chambre"] = "Set Level 100"
        end
    elseif (os.date("%H:%M") == "07:03") then
        print("il est 07:03")
        if (otherdevices["Lampe Chambre"] == "On") then
            commandArray["Lampe Chambre"] = "Set Level 0"
        end
    elseif (os.date("%H:%M") == "07:40") then
        print("il est 07:40")
        if (otherdevices["Lampe Chambre"] == "On") then
            commandArray["Lampe Chambre"] = "Set Level 0"
        end
        if (otherdevices["Lampe Chambre"] == "Off") then
            commandArray["Group Séjour"] = "Off"
        end
    end
end

return commandArray

