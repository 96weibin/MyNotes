
//GLOBAL SPACE
///////////////////Retrieve some cached data/////////////////////
    var flowratecache = SimulatorDataPersistence.getCache("M001_ParamsInitData");
    if(flowratecache === undefined || flowratecache === null){
        flowratecache = null;
        SimulatorDataPersistence.setCache("M001_ParamsInitData", flowratecache);
            
    }

    //INPUT SECTION
    ////////////////////Read simulation values for different resources//////////////////////
    const variables = [
        //"Units.AtmTwr1.Parameters",
        "Tanks.T-004.LimitsViolated",
        "Tanks.T-004.Limits",
        "Tanks.T-004.Volume",
        "Tanks.T-002.LimitsViolated",
        "Tanks.T-002.Limits",
        "Tanks.T-002.Volume",
        "Tanks.T-003.LimitsViolated",
        "Tanks.T-003.Limits",
        "Tanks.T-003.Volume",
        "Units.CU-001.Parameters",
        "Units.AtmTwr1.Parameters.CDU1, Mode 1 - NK1",
        "Units.M-001.Parameters.M-001_param1",
        "Units.M-001.Parameters.Kero Hydrotreater-KTF",
        "Model.PeriodStart"
    ];

    var values = [];
    values = Simulator.getData(variables);
    
    Object.keys(values).forEach(function(key){
        if(values[key]===undefined)
            Log.error("Unable to retrieve values for one or more variables"); 
    } );
    
    //CUSTOM LOGIC to make scheduling decisions on unit parameters
    ///////////////////////Custom Calculations: manioulate the simulation data/////////////////////////////////
    //Current period
    var curPeriod = values["Model.PeriodStart"];
    //const targetDate = new Date('February 05, 2022 00:00:00');
    const targetDate = new Date("02/05/2022");
    const curDate = new Date(curPeriod);
    let curdtnum = Number(curDate);
    let trgdtnum = Number(targetDate);

    //Custom unit param to take action
    let cuparams = values["Units.CU-001.Parameters"];
    let tankViolationEnum = cuparams["TankViolation"]["Value"];

    //Tank limits, violation and inventory
     let t004violation = values["Tanks.T-004.LimitsViolated"];
    let t004Limits = values["Tanks.T-004.Limits"];
    let t004Inv = values["Tanks.T-004.Volume"];
    let t004newInv = t004Inv;

    let t002violation = values["Tanks.T-002.LimitsViolated"];
    let t002Limits = values["Tanks.T-002.Limits"];
    let t002Inv = values["Tanks.T-002.Volume"];
    let t002newInv = t002Inv;

    let t003violation = values["Tanks.T-003.LimitsViolated"];
    let t003Limits = values["Tanks.T-003.Limits"];
    let t003Inv = values["Tanks.T-003.Volume"];
    let t003newInv = t003Inv;

    const tnkadjdate = new Date('February 05, 2022 00:00:00');
    let adjdtnum = Number(tnkadjdate);
    if(tankViolationEnum === "T-004"){
        if(t004violation === true){           
            if(curdtnum >= adjdtnum){
                if(t004newInv < t004Limits[0])
                    t004newInv = t004Limits[0];
                if(t004newInv > t004Limits[1])
                    t004newInv = t004Limits[1];
            }
            Log.warning("T-004: limits violation");
        }
    } 
    if(tankViolationEnum === "T-002"){
        if(t002violation === true){
            if(curdtnum >= adjdtnum){
                if(t002newInv < t002Limits[0])
                    t002newInv = t002Limits[0];
                if(t002newInv > t002Limits[1])
                    t002newInv = t002Limits[1];
            }
            Log.warning("T-002: limits violation");
        }
    } 
    if(tankViolationEnum === "T-003"){
        if(t003violation === true){
            if(curdtnum > adjdtnum){
                if(t003newInv < t003Limits[0])
                    t003newInv = t003Limits[0];
                if(t003newInv > t003Limits[1])
                    t003newInv = t003Limits[1];
            }
            Log.warning("T-003: limits violation");
        }
    } 
   
    //Mixer/Splitter parameter operations
    var mixerparam1 = values["Units.M-001.Parameters.M-001_param1"];
    var mixerparam2 = values["Units.M-001.Parameters.Kero Hydrotreater-KTF"];
    var param1Val = mixerparam1.Value;
    var param2Val = mixerparam2.Value;
    
    var tower1NK1param = 300;

    var flowrateChangeData = [];  
     if(curdtnum >= trgdtnum){
         if(flowratecache === null){
             flowrateChangeData[0] = param1Val;
             flowrateChangeData[1] = param2Val;
             //cache it
            SimulatorDataPersistence.setCache("M001_ParamsInitData", flowrateChangeData);
         }
        tower1NK1param = 750;
        param1Val = 60;
        param2Val = 40;
        t003Limits[0] = 50;
        t003Limits[1] = 150;
        Log.info("M-001: Feed Rate Changed on {curPeriod}");
     }
     let streamkeroLimits = [10,20];
    //OUTPUT SECTION: modeify unit parameters, tank inventories, stream data etc
    ///////////////////////Update the simulated data with changes (from custom calculations)///////////////////
    const outputs = {
            "Units.AtmTwr1.Parameters.CDU1, Mode 1 - NK1":tower1NK1param,
            "Units.M-001.Parameters.M-001_param1":param1Val,
            "Units.M-001.Parameters.Kero Hydrotreater-KTF":param2Val,
            "Streams.Kero Hydrotreater-KTF.Limits":streamkeroLimits,
            "Tanks.T-004.Volume":t004newInv,
            "Tanks.T-002.Volume":t002newInv,
            "Tanks.T-003.Limits":t003Limits,
        };
    Simulator.setData(outputs); 

   


var values = Simulator.getData([
    "Model.PeriodStart",
    "Tanks.T-001.Volume",
    "Tanks.T-001.Limits", 
    ]);
//tank inventory
var t01Valume = values["Tanks.T-001.Volume"];
var t01MinLimt = values["Tanks.T-001.Limits"][0];
var t01MaxLimt = values["Tanks.T-001.Limits"][1];
var curPeriod = values["Model.PeriodStart"];
var targetDate = "3/12/2022";

if(new Date(curPeriod).getTime() < new Date(targetDate).getTime())
if(t01Valume < t01MinLimt){
    Log.warning(t01Valume + " : less than min");
} else if(t01Valume > t01MaxLimt) {
    Log.error(t01Valume + " : great than max");
} 


Log.error("cu02 error test");
Log.warning("cu02 warning test");