commandArray = {}

jourF = false

OFF = "Set Level 0"
HORSGEL = "Set Level 10"
ECO = "Set Level 20"
CONFORT = "Set Level 30"

if (otherdevices["Présence"] == "Normal") then
    
    for deviceName,deviceValue in pairs(otherdevices) do
        if (deviceName=='Jour férié') then
            if deviceValue == "On" then
                print("Jour férié")
                jourF = true
            end
        end
    end
    
    week = os.date("%A") ~= "Saturday" and os.date("%A") ~= "Sunday"
    
    if (week) then -- la semaine
        if (not jourF) then -- pas un jour férié
            if (os.date("%H:%M") == "05:00") then
                print("il est 05:00")
                commandArray["Consigne Chauffage"] = CONFORT
            elseif (os.date("%H:%M") == "07:00") then
                print("il est 07:00")
                commandArray["Consigne Chauffage"] = ECO
            elseif (os.date("%H:%M") == "17:00") then
                print("il est 17:00")
                commandArray["Consigne Chauffage"] = CONFORT
            elseif (os.date("%H:%M") == "22:00") then
                print("il est 12:00")
                commandArray["Consigne Chauffage"] = ECO
            end
        else
            print("semaine et jour férié")
            if (os.date("%H:%M") == "08:00") then
                print("il est 08:00")
                commandArray["Consigne Chauffage"] = CONFORT
            elseif (os.date("%H:%M") == "22:00") then
                print("il est 22:00")
                commandArray["Consigne Chauffage"] = ECO
            end
        end
    else -- le weekend
        if (os.date("%H:%M") == "08:00") then
            print("il est 08:00")
            commandArray["Consigne Chauffage"] = CONFORT
        elseif (os.date("%H:%M") == "22:00") then
            print("il est 22:00")
            commandArray["Consigne Chauffage"] = ECO
        end
    end

elseif(otherdevices["Présence"] == "VacancesPrésent") then -- si en vacances mais présent
    print("VacancesPrésent")
    if (os.date("%H:%M") == "08:00") then
        print("il est 08:00")
        commandArray["Consigne Chauffage"] = CONFORT
    elseif (os.date("%H:%M") == "22:00") then
        print("il est 22:00")
        commandArray["Consigne Chauffage"] = ECO
    end
    
elseif (otherdevices["Présence"] == "VacancesAbsent") then -- si en vacances mais absent
    print("mode eco, VacancesAbsent")
    commandArray["Consigne Chauffage"] = ECO
end

return commandArray
