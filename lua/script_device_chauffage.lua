commandArray = {}

--if(devicechanged["Consigne Chauffage"] ~= nil) then
--    if (otherdevices_svalues['Consigne Chauffage'] == "Off") then
--        commandArray['RadiateurGauche'] = "Set Level 0"
--        commandArray['RadiateurDroit'] = "Set Level 0"
--    elseif (otherdevices_svalues['Consigne Chauffage'] == "HorsGel") then
--        ommandArray['RadiateurGauche'] = "Set Level 15"
 --       commandArray['RadiateurDroit'] = "Set Level 15"
--    elseif (otherdevices_svalues['Consigne Chauffage'] == "Eco") then
 --       commandArray['RadiateurGauche'] = "Set Level 25"
--        commandArray['RadiateurDroit'] = "Set Level 25"
--    elseif (otherdevices_svalues['Consigne Chauffage'] == "Confort") then
--        commandArray['RadiateurGauche'] = "Set Level 100"
--        commandArray['RadiateurDroit'] = "Set Level 100"
--    end
--end

if(devicechanged == nil) then
    -- do nothings, prevent error
elseif (devicechanged["Consigne Chauffage"] == "Off") then
    commandArray['RadiateurGauche'] = "Set Level 0"
    commandArray['RadiateurDroit'] = "Set Level 0"
elseif (devicechanged["Consigne Chauffage"] == "HorsGel") then
    commandArray['RadiateurGauche'] = "Set Level 15"
    commandArray['RadiateurDroit'] = "Set Level 15"
elseif (devicechanged["Consigne Chauffage"] == "Eco") then
    commandArray['RadiateurGauche'] = "Set Level 25"
    commandArray['RadiateurDroit'] = "Set Level 25"
elseif (devicechanged["Consigne Chauffage"] == "Confort") then
    commandArray['RadiateurGauche'] = "Set Level 100"
    commandArray['RadiateurDroit'] = "Set Level 100"
end

return commandArray

