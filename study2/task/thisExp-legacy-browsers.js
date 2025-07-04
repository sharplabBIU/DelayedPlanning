/**************** 
 * Thisexp *
 ****************/


// store info about the experiment session:
let expName = 'thisExp';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
flowScheduler.add(consent2RoutineBegin());
flowScheduler.add(consent2RoutineEachFrame());
flowScheduler.add(consent2RoutineEnd());
flowScheduler.add(questionnaire_startRoutineBegin());
flowScheduler.add(questionnaire_startRoutineEachFrame());
flowScheduler.add(questionnaire_startRoutineEnd());
flowScheduler.add(PSWQ1RoutineBegin());
flowScheduler.add(PSWQ1RoutineEachFrame());
flowScheduler.add(PSWQ1RoutineEnd());
flowScheduler.add(PSWQ2RoutineBegin());
flowScheduler.add(PSWQ2RoutineEachFrame());
flowScheduler.add(PSWQ2RoutineEnd());
flowScheduler.add(PSWQ3RoutineBegin());
flowScheduler.add(PSWQ3RoutineEachFrame());
flowScheduler.add(PSWQ3RoutineEnd());
flowScheduler.add(PSWQ4RoutineBegin());
flowScheduler.add(PSWQ4RoutineEachFrame());
flowScheduler.add(PSWQ4RoutineEnd());
flowScheduler.add(PSWQ5RoutineBegin());
flowScheduler.add(PSWQ5RoutineEachFrame());
flowScheduler.add(PSWQ5RoutineEnd());
flowScheduler.add(PSWQ6RoutineBegin());
flowScheduler.add(PSWQ6RoutineEachFrame());
flowScheduler.add(PSWQ6RoutineEnd());
flowScheduler.add(PSWQ7RoutineBegin());
flowScheduler.add(PSWQ7RoutineEachFrame());
flowScheduler.add(PSWQ7RoutineEnd());
flowScheduler.add(PSWQ8RoutineBegin());
flowScheduler.add(PSWQ8RoutineEachFrame());
flowScheduler.add(PSWQ8RoutineEnd());
flowScheduler.add(PSWQ9RoutineBegin());
flowScheduler.add(PSWQ9RoutineEachFrame());
flowScheduler.add(PSWQ9RoutineEnd());
flowScheduler.add(PSWQ10RoutineBegin());
flowScheduler.add(PSWQ10RoutineEachFrame());
flowScheduler.add(PSWQ10RoutineEnd());
flowScheduler.add(PSWQ11RoutineBegin());
flowScheduler.add(PSWQ11RoutineEachFrame());
flowScheduler.add(PSWQ11RoutineEnd());
flowScheduler.add(PSWQ12RoutineBegin());
flowScheduler.add(PSWQ12RoutineEachFrame());
flowScheduler.add(PSWQ12RoutineEnd());
flowScheduler.add(PSWQ13RoutineBegin());
flowScheduler.add(PSWQ13RoutineEachFrame());
flowScheduler.add(PSWQ13RoutineEnd());
flowScheduler.add(PSWQ14RoutineBegin());
flowScheduler.add(PSWQ14RoutineEachFrame());
flowScheduler.add(PSWQ14RoutineEnd());
flowScheduler.add(PSWQ15RoutineBegin());
flowScheduler.add(PSWQ15RoutineEachFrame());
flowScheduler.add(PSWQ15RoutineEnd());
flowScheduler.add(PSWQ16RoutineBegin());
flowScheduler.add(PSWQ16RoutineEachFrame());
flowScheduler.add(PSWQ16RoutineEnd());
flowScheduler.add(q2_instructionsRoutineBegin());
flowScheduler.add(q2_instructionsRoutineEachFrame());
flowScheduler.add(q2_instructionsRoutineEnd());
flowScheduler.add(AM1RoutineBegin());
flowScheduler.add(AM1RoutineEachFrame());
flowScheduler.add(AM1RoutineEnd());
flowScheduler.add(AM2RoutineBegin());
flowScheduler.add(AM2RoutineEachFrame());
flowScheduler.add(AM2RoutineEnd());
flowScheduler.add(AM3RoutineBegin());
flowScheduler.add(AM3RoutineEachFrame());
flowScheduler.add(AM3RoutineEnd());
flowScheduler.add(AM4RoutineBegin());
flowScheduler.add(AM4RoutineEachFrame());
flowScheduler.add(AM4RoutineEnd());
flowScheduler.add(AM5RoutineBegin());
flowScheduler.add(AM5RoutineEachFrame());
flowScheduler.add(AM5RoutineEnd());
flowScheduler.add(q3_instructionsRoutineBegin());
flowScheduler.add(q3_instructionsRoutineEachFrame());
flowScheduler.add(q3_instructionsRoutineEnd());
flowScheduler.add(SPQ1RoutineBegin());
flowScheduler.add(SPQ1RoutineEachFrame());
flowScheduler.add(SPQ1RoutineEnd());
flowScheduler.add(SPQ2RoutineBegin());
flowScheduler.add(SPQ2RoutineEachFrame());
flowScheduler.add(SPQ2RoutineEnd());
flowScheduler.add(SPQ3RoutineBegin());
flowScheduler.add(SPQ3RoutineEachFrame());
flowScheduler.add(SPQ3RoutineEnd());
flowScheduler.add(SPQ4RoutineBegin());
flowScheduler.add(SPQ4RoutineEachFrame());
flowScheduler.add(SPQ4RoutineEnd());
flowScheduler.add(SPQ5RoutineBegin());
flowScheduler.add(SPQ5RoutineEachFrame());
flowScheduler.add(SPQ5RoutineEnd());
flowScheduler.add(SPQ6RoutineBegin());
flowScheduler.add(SPQ6RoutineEachFrame());
flowScheduler.add(SPQ6RoutineEnd());
flowScheduler.add(SPQ7RoutineBegin());
flowScheduler.add(SPQ7RoutineEachFrame());
flowScheduler.add(SPQ7RoutineEnd());
flowScheduler.add(SPQ8RoutineBegin());
flowScheduler.add(SPQ8RoutineEachFrame());
flowScheduler.add(SPQ8RoutineEnd());
flowScheduler.add(SPQ9RoutineBegin());
flowScheduler.add(SPQ9RoutineEachFrame());
flowScheduler.add(SPQ9RoutineEnd());
flowScheduler.add(SPQ10RoutineBegin());
flowScheduler.add(SPQ10RoutineEachFrame());
flowScheduler.add(SPQ10RoutineEnd());
flowScheduler.add(SQP11RoutineBegin());
flowScheduler.add(SQP11RoutineEachFrame());
flowScheduler.add(SQP11RoutineEnd());
flowScheduler.add(SPQ12RoutineBegin());
flowScheduler.add(SPQ12RoutineEachFrame());
flowScheduler.add(SPQ12RoutineEnd());
flowScheduler.add(SPQ13RoutineBegin());
flowScheduler.add(SPQ13RoutineEachFrame());
flowScheduler.add(SPQ13RoutineEnd());
flowScheduler.add(SPQ14RoutineBegin());
flowScheduler.add(SPQ14RoutineEachFrame());
flowScheduler.add(SPQ14RoutineEnd());
flowScheduler.add(SPQ15RoutineBegin());
flowScheduler.add(SPQ15RoutineEachFrame());
flowScheduler.add(SPQ15RoutineEnd());
flowScheduler.add(SPQ16RoutineBegin());
flowScheduler.add(SPQ16RoutineEachFrame());
flowScheduler.add(SPQ16RoutineEnd());
flowScheduler.add(SPQ17RoutineBegin());
flowScheduler.add(SPQ17RoutineEachFrame());
flowScheduler.add(SPQ17RoutineEnd());
flowScheduler.add(SPQ18RoutineBegin());
flowScheduler.add(SPQ18RoutineEachFrame());
flowScheduler.add(SPQ18RoutineEnd());
flowScheduler.add(SPQ19RoutineBegin());
flowScheduler.add(SPQ19RoutineEachFrame());
flowScheduler.add(SPQ19RoutineEnd());
flowScheduler.add(SPQ20RoutineBegin());
flowScheduler.add(SPQ20RoutineEachFrame());
flowScheduler.add(SPQ20RoutineEnd());
flowScheduler.add(SPQ21RoutineBegin());
flowScheduler.add(SPQ21RoutineEachFrame());
flowScheduler.add(SPQ21RoutineEnd());
flowScheduler.add(SPQ22RoutineBegin());
flowScheduler.add(SPQ22RoutineEachFrame());
flowScheduler.add(SPQ22RoutineEnd());
flowScheduler.add(q4_instructionsRoutineBegin());
flowScheduler.add(q4_instructionsRoutineEachFrame());
flowScheduler.add(q4_instructionsRoutineEnd());
flowScheduler.add(SS1RoutineBegin());
flowScheduler.add(SS1RoutineEachFrame());
flowScheduler.add(SS1RoutineEnd());
flowScheduler.add(SS2RoutineBegin());
flowScheduler.add(SS2RoutineEachFrame());
flowScheduler.add(SS2RoutineEnd());
flowScheduler.add(SS3RoutineBegin());
flowScheduler.add(SS3RoutineEachFrame());
flowScheduler.add(SS3RoutineEnd());
flowScheduler.add(SS4RoutineBegin());
flowScheduler.add(SS4RoutineEachFrame());
flowScheduler.add(SS4RoutineEnd());
flowScheduler.add(SS5RoutineBegin());
flowScheduler.add(SS5RoutineEachFrame());
flowScheduler.add(SS5RoutineEnd());
flowScheduler.add(SS6RoutineBegin());
flowScheduler.add(SS6RoutineEachFrame());
flowScheduler.add(SS6RoutineEnd());
flowScheduler.add(SS7RoutineBegin());
flowScheduler.add(SS7RoutineEachFrame());
flowScheduler.add(SS7RoutineEnd());
flowScheduler.add(SS8RoutineBegin());
flowScheduler.add(SS8RoutineEachFrame());
flowScheduler.add(SS8RoutineEnd());
flowScheduler.add(SS9RoutineBegin());
flowScheduler.add(SS9RoutineEachFrame());
flowScheduler.add(SS9RoutineEnd());
flowScheduler.add(SS10RoutineBegin());
flowScheduler.add(SS10RoutineEachFrame());
flowScheduler.add(SS10RoutineEnd());
const instructions_get_rightLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(instructions_get_rightLoopBegin(instructions_get_rightLoopScheduler));
flowScheduler.add(instructions_get_rightLoopScheduler);
flowScheduler.add(instructions_get_rightLoopEnd);




















flowScheduler.add(start_learningRoutineBegin());
flowScheduler.add(start_learningRoutineEachFrame());
flowScheduler.add(start_learningRoutineEnd());
const learning_phaseLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(learning_phaseLoopBegin(learning_phaseLoopScheduler));
flowScheduler.add(learning_phaseLoopScheduler);
flowScheduler.add(learning_phaseLoopEnd);




































flowScheduler.add(break_routineRoutineBegin());
flowScheduler.add(break_routineRoutineEachFrame());
flowScheduler.add(break_routineRoutineEnd());
const instructions_planning_get_rightLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(instructions_planning_get_rightLoopBegin(instructions_planning_get_rightLoopScheduler));
flowScheduler.add(instructions_planning_get_rightLoopScheduler);
flowScheduler.add(instructions_planning_get_rightLoopEnd);









flowScheduler.add(see_planning_trialsRoutineBegin());
flowScheduler.add(see_planning_trialsRoutineEachFrame());
flowScheduler.add(see_planning_trialsRoutineEnd());
flowScheduler.add(instructions_planning_newRoutineBegin());
flowScheduler.add(instructions_planning_newRoutineEachFrame());
flowScheduler.add(instructions_planning_newRoutineEnd());
flowScheduler.add(planning_2_instructionsRoutineBegin());
flowScheduler.add(planning_2_instructionsRoutineEachFrame());
flowScheduler.add(planning_2_instructionsRoutineEnd());
flowScheduler.add(instructions_planning_new3RoutineBegin());
flowScheduler.add(instructions_planning_new3RoutineEachFrame());
flowScheduler.add(instructions_planning_new3RoutineEnd());
flowScheduler.add(practice_planning_outcomesRoutineBegin());
flowScheduler.add(practice_planning_outcomesRoutineEachFrame());
flowScheduler.add(practice_planning_outcomesRoutineEnd());
flowScheduler.add(immediate_rewar_lessonRoutineBegin());
flowScheduler.add(immediate_rewar_lessonRoutineEachFrame());
flowScheduler.add(immediate_rewar_lessonRoutineEnd());
flowScheduler.add(lesson_practiceRoutineBegin());
flowScheduler.add(lesson_practiceRoutineEachFrame());
flowScheduler.add(lesson_practiceRoutineEnd());
flowScheduler.add(lesson_practice_2RoutineBegin());
flowScheduler.add(lesson_practice_2RoutineEachFrame());
flowScheduler.add(lesson_practice_2RoutineEnd());
flowScheduler.add(start_real_planningRoutineBegin());
flowScheduler.add(start_real_planningRoutineEachFrame());
flowScheduler.add(start_real_planningRoutineEnd());
const planning_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(planning_loopLoopBegin(planning_loopLoopScheduler));
flowScheduler.add(planning_loopLoopScheduler);
flowScheduler.add(planning_loopLoopEnd);






flowScheduler.add(planning_pathsRoutineBegin());
flowScheduler.add(planning_pathsRoutineEachFrame());
flowScheduler.add(planning_pathsRoutineEnd());
const remember_planning_pathsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(remember_planning_pathsLoopBegin(remember_planning_pathsLoopScheduler));
flowScheduler.add(remember_planning_pathsLoopScheduler);
flowScheduler.add(remember_planning_pathsLoopEnd);




flowScheduler.add(total_score_planningRoutineBegin());
flowScheduler.add(total_score_planningRoutineEachFrame());
flowScheduler.add(total_score_planningRoutineEnd());
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stage2_4_practice.csv', 'path': 'stage2_4_practice.csv'},
    {'name': 'planet.png', 'path': 'planet.png'},
    {'name': 'basket.png', 'path': 'basket.png'},
    {'name': 'image_train_press.xlsx', 'path': 'image_train_press.xlsx'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'images/backpack.png', 'path': 'images/backpack.png'},
    {'name': 'images/bowtie.png', 'path': 'images/bowtie.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
    {'name': 'images/car.png', 'path': 'images/car.png'},
    {'name': 'images/lamp.png', 'path': 'images/lamp.png'},
    {'name': 'images/zebra.png', 'path': 'images/zebra.png'},
    {'name': 'images/cat.png', 'path': 'images/cat.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'quiz_1.xlsx', 'path': 'quiz_1.xlsx'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'images/backpack.png', 'path': 'images/backpack.png'},
    {'name': 'images/hammer.png', 'path': 'images/hammer.png'},
    {'name': 'images/lamp.png', 'path': 'images/lamp.png'},
    {'name': 'images/zebra.png', 'path': 'images/zebra.png'},
    {'name': 'images/car.png', 'path': 'images/car.png'},
    {'name': 'images/bowtie.png', 'path': 'images/bowtie.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
    {'name': 'images/hourglass.png', 'path': 'images/hourglass.png'},
    {'name': 'images/cat.png', 'path': 'images/cat.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'image_train_press.xlsx', 'path': 'image_train_press.xlsx'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'images/backpack.png', 'path': 'images/backpack.png'},
    {'name': 'images/bowtie.png', 'path': 'images/bowtie.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
    {'name': 'images/car.png', 'path': 'images/car.png'},
    {'name': 'images/lamp.png', 'path': 'images/lamp.png'},
    {'name': 'images/zebra.png', 'path': 'images/zebra.png'},
    {'name': 'images/cat.png', 'path': 'images/cat.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'quiz_1.xlsx', 'path': 'quiz_1.xlsx'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'images/backpack.png', 'path': 'images/backpack.png'},
    {'name': 'images/hammer.png', 'path': 'images/hammer.png'},
    {'name': 'images/lamp.png', 'path': 'images/lamp.png'},
    {'name': 'images/zebra.png', 'path': 'images/zebra.png'},
    {'name': 'images/car.png', 'path': 'images/car.png'},
    {'name': 'images/bowtie.png', 'path': 'images/bowtie.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
    {'name': 'images/hourglass.png', 'path': 'images/hourglass.png'},
    {'name': 'images/cat.png', 'path': 'images/cat.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'forgetting1.xlsx', 'path': 'forgetting1.xlsx'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'images/backpack.png', 'path': 'images/backpack.png'},
    {'name': 'images/lamp.png', 'path': 'images/lamp.png'},
    {'name': 'images/zebra.png', 'path': 'images/zebra.png'},
    {'name': 'images/bowtie.png', 'path': 'images/bowtie.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
    {'name': 'images/car.png', 'path': 'images/car.png'},
    {'name': 'images/cat.png', 'path': 'images/cat.png'},
    {'name': 'planning_trials.xlsx', 'path': 'planning_trials.xlsx'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'images/zebra.png', 'path': 'images/zebra.png'},
    {'name': 'images/backpack.png', 'path': 'images/backpack.png'},
    {'name': 'images/hourglass.png', 'path': 'images/hourglass.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
    {'name': 'images/lamp.png', 'path': 'images/lamp.png'},
    {'name': 'images/cat.png', 'path': 'images/cat.png'},
    {'name': 'forgetting1.xlsx', 'path': 'forgetting1.xlsx'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'images/backpack.png', 'path': 'images/backpack.png'},
    {'name': 'images/lamp.png', 'path': 'images/lamp.png'},
    {'name': 'images/zebra.png', 'path': 'images/zebra.png'},
    {'name': 'images/bowtie.png', 'path': 'images/bowtie.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
    {'name': 'images/car.png', 'path': 'images/car.png'},
    {'name': 'images/cat.png', 'path': 'images/cat.png'},
    {'name': 'consent1.png', 'path': 'consent1.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'consent2.png', 'path': 'consent2.png'},
    {'name': 'apple.png', 'path': 'apple.png'},
    {'name': 'basket.png', 'path': 'basket.png'},
    {'name': 'fireworks.png', 'path': 'fireworks.png'},
    {'name': 'tree.png', 'path': 'tree.png'},
    {'name': 'images/knight.png', 'path': 'images/knight.png'},
    {'name': 'images/computer.png', 'path': 'images/computer.png'},
    {'name': 'images/baby.png', 'path': 'images/baby.png'},
    {'name': 'planet.png', 'path': 'planet.png'},
    {'name': 'images/toothbrush.png', 'path': 'images/toothbrush.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=CHPYNJMX', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var consentClock;
var image_11;
var consent1_next;
var text_89;
var consent2Clock;
var image_13;
var consent1_next_2;
var text_90;
var questionnaire_startClock;
var text_33;
var PSWQ1Clock;
var text_36;
var text_56;
var text_57;
var key_resp_3;
var PSWQ2Clock;
var text_58;
var text_59;
var text_60;
var key_resp_13;
var PSWQ3Clock;
var text_61;
var text_62;
var text_63;
var key_resp_14;
var PSWQ4Clock;
var text_64;
var text_65;
var text_66;
var key_resp_15;
var PSWQ5Clock;
var text_67;
var text_68;
var text_69;
var key_resp_16;
var PSWQ6Clock;
var text_76;
var text_77;
var text_78;
var key_resp_25;
var PSWQ7Clock;
var text_79;
var text_80;
var text_81;
var key_resp_26;
var PSWQ8Clock;
var text_82;
var text_83;
var text_84;
var key_resp_27;
var PSWQ9Clock;
var text_85;
var text_86;
var text_87;
var key_resp_28;
var PSWQ10Clock;
var text_88;
var text_91;
var text_92;
var key_resp_29;
var PSWQ11Clock;
var text_93;
var text_94;
var text_95;
var key_resp_30;
var PSWQ12Clock;
var text_96;
var text_97;
var text_98;
var key_resp_31;
var PSWQ13Clock;
var text_99;
var text_100;
var text_101;
var key_resp_32;
var PSWQ14Clock;
var text_102;
var text_103;
var text_104;
var key_resp_33;
var PSWQ15Clock;
var text_105;
var text_106;
var text_107;
var key_resp_34;
var PSWQ16Clock;
var text_108;
var text_109;
var text_110;
var key_resp_35;
var q2_instructionsClock;
var text_155;
var AM1Clock;
var text_156;
var text_157;
var text_158;
var key_resp_41;
var AM2Clock;
var text_159;
var text_160;
var text_161;
var key_resp_42;
var AM3Clock;
var text_162;
var text_163;
var text_164;
var key_resp_43;
var AM4Clock;
var text_165;
var text_166;
var text_167;
var key_resp_44;
var AM5Clock;
var text_168;
var text_169;
var text_170;
var key_resp_45;
var q3_instructionsClock;
var text_171;
var SPQ1Clock;
var text_173;
var text_174;
var key_resp_46;
var SPQ2Clock;
var text_175;
var text_176;
var key_resp_47;
var SPQ3Clock;
var text_177;
var text_178;
var key_resp_48;
var SPQ4Clock;
var text_179;
var text_180;
var key_resp_49;
var SPQ5Clock;
var text_181;
var text_182;
var key_resp_50;
var SPQ6Clock;
var text_183;
var text_184;
var key_resp_51;
var SPQ7Clock;
var text_185;
var text_186;
var key_resp_52;
var SPQ8Clock;
var text_187;
var text_188;
var key_resp_53;
var SPQ9Clock;
var text_189;
var text_190;
var key_resp_54;
var SPQ10Clock;
var text_191;
var text_192;
var key_resp_55;
var SQP11Clock;
var text_193;
var text_194;
var key_resp_56;
var SPQ12Clock;
var text_195;
var text_196;
var key_resp_57;
var SPQ13Clock;
var text_197;
var text_198;
var key_resp_58;
var SPQ14Clock;
var text_199;
var text_200;
var key_resp_59;
var SPQ15Clock;
var text_201;
var text_202;
var key_resp_60;
var SPQ16Clock;
var text_203;
var text_204;
var key_resp_61;
var SPQ17Clock;
var text_205;
var text_206;
var key_resp_62;
var SPQ18Clock;
var text_207;
var text_208;
var key_resp_63;
var SPQ19Clock;
var text_209;
var text_210;
var key_resp_64;
var SPQ20Clock;
var text_211;
var text_212;
var key_resp_65;
var SPQ21Clock;
var text_213;
var text_214;
var key_resp_66;
var SPQ22Clock;
var text_215;
var text_216;
var key_resp_67;
var q4_instructionsClock;
var text_172;
var SS1Clock;
var text_217;
var text_218;
var text_219;
var key_resp_68;
var SS2Clock;
var text_220;
var text_221;
var text_222;
var key_resp_69;
var SS3Clock;
var text_223;
var text_224;
var text_225;
var key_resp_70;
var SS4Clock;
var text_226;
var text_227;
var text_228;
var key_resp_71;
var SS5Clock;
var text_229;
var text_230;
var text_231;
var key_resp_72;
var SS6Clock;
var text_232;
var text_233;
var text_234;
var key_resp_73;
var SS7Clock;
var text_235;
var text_236;
var text_237;
var key_resp_74;
var SS8Clock;
var text_238;
var text_239;
var text_240;
var key_resp_75;
var SS9Clock;
var text_241;
var text_242;
var text_243;
var key_resp_76;
var SS10Clock;
var text_244;
var text_245;
var text_246;
var key_resp_77;
var instructionsClock;
var incorrect_actions;
var cogmap;
var cogmap_replanning;
var current_image;
var current_image2;
var current_image3;
var current_image4;
var alternative_image;
var instruction_test;
var end_instructions;
var second_instructionsClock;
var key_resp_2;
var text_22;
var third_instructionsClock;
var responseleft;
var text_23;
var instructions4Clock;
var text_153;
var practice1Clock;
var image_22;
var key_resp_10;
var text_40;
var practice1_resultClock;
var image_20;
var next_trialClock;
var next_trial_text;
var practice1_quizClock;
var basket_2;
var fireworks_2;
var tree_2;
var text_24;
var text_25;
var text_27;
var practice_answer;
var text_26;
var practice1_quizfeedbackClock;
var text_30;
var memory_quiz_instructionsClock;
var text_75;
var key_resp_23;
var quiz1_iClock;
var text_43;
var key_resp_17;
var quiz2_iClock;
var text_70;
var key_resp_18;
var quiz3Clock;
var text_71;
var key_resp_19;
var quiz4Clock;
var text_72;
var key_resp_20;
var quiz_feedbackClock;
var result_q_instr;
var start_learningClock;
var text_31;
var key_resp_7;
var learn1Clock;
var key_resp;
var image_1;
var text;
var check_incorrect1Clock;
var text_incorrect_2;
var learn2Clock;
var image_2;
var counter_quizzes_roundClock;
var betweenClock;
var text_2;
var quizClock;
var target_quiz1;
var question_quiz1;
var answer_quiz1;
var answer1;
var answer2;
var answer3;
var answer4;
var a1;
var a2;
var a3;
var a4;
var back_to_learnClock;
var text_8;
var check_incorrectClock;
var text_incorrect;
var quiz2Clock;
var target_quiz1_2;
var question_quiz1_2;
var answer_quiz1_2;
var answer1_2;
var answer2_2;
var answer3_2;
var answer4_2;
var a1_2;
var a2_2;
var a3_2;
var a4_2;
var planning_pathsClock;
var text_149;
var key_resp_40;
var text_49;
var forgetting_paths1Clock;
var question_quiz1_3;
var answer_quiz1_3;
var answer1_3;
var answer2_3;
var answer3_3;
var a1_3;
var a2_3;
var text_146;
var planningpathstraining2Clock;
var question_quiz1_5;
var answer_quiz1_5;
var answer1_5;
var answer2_5;
var answer3_5;
var a1_5;
var a2_5;
var text_152;
var correct_forget_pathsClock;
var next_trial_text_2;
var text_151;
var total_score_planningClock;
var next_trial_text_3;
var text_150;
var break_routineClock;
var text_9;
var instructions_rewardClock;
var instructions_rewardstage;
var key_resp_11;
var text_46;
var instructions_planning_2Clock;
var text_50;
var key_resp_9;
var directions_dict;
var action;
var correct_quiz;
var percent_correct;
var text_correct;
var instructions_example_trialClock;
var text_13;
var R1_5;
var R2_5;
var rew1_5;
var rew2_5;
var text_21;
var plan2_response_2;
var current_image_decision2_2;
var long_term_reward_instructionsClock;
var instructions_rewardstage_2;
var key_resp_12;
var text_45;
var quiz_planning_1Clock;
var text_47;
var key_resp_21;
var quiz_planning_2Clock;
var text_73;
var key_resp_22;
var quiz_planning_3Clock;
var text_74;
var key_resp_24;
var see_planning_trialsClock;
var text_48;
var key_resp_8;
var instructions_planning_newClock;
var text_32;
var R1_6;
var R2_6;
var rew1_6;
var rew2_6;
var plan2_response_3;
var text_34;
var text_41;
var text_114;
var text_128;
var planning_2_instructionsClock;
var text_52;
var R1_9;
var R2_9;
var rew1_9;
var rew2_9;
var text_53;
var plan2_response_6;
var current_image_decision2_5;
var text_115;
var text_129;
var instructions_planning_new3Clock;
var text_136;
var R1_11;
var R2_11;
var rew1_11;
var rew2_11;
var plan2_response_5;
var current_image_decision2_6;
var text_137;
var text_138;
var text_139;
var text_140;
var practice_planning_outcomesClock;
var image_6;
var text_141;
var text_142;
var text_143;
var immediate_rewar_lessonClock;
var text_148;
var key_resp_39;
var lesson_practiceClock;
var text_144;
var key_resp_37;
var lesson_practice_2Clock;
var text_145;
var key_resp_38;
var start_real_planningClock;
var text_42;
var key_resp_6;
var plan1_info_2Clock;
var text_5;
var R1;
var R2;
var rew1;
var rew2;
var text_6;
var plan1_response;
var babyleft;
var toothbrushright;
var text_117;
var text_120;
var plan2_infoClock;
var text_7;
var R1_2;
var R2_2;
var rew1_2;
var rew2_2;
var text_10;
var plan2_response;
var current_image_decision2;
var text_118;
var text_121;
var plan3_infoClock;
var text_14;
var R1_3;
var R2_3;
var rew1_3;
var rew2_3;
var text_15;
var plan3_response;
var current_image_decision3;
var text_122;
var text_123;
var planning4Clock;
var image_4;
var text_19;
var text_119;
var text_131;
var endClock;
var text_20;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.05], size : [0.65, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  consent1_next = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_89 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_89',
    text: 'Click SPACE to Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "consent2"
  consent2Clock = new util.Clock();
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.1], size : [0.65, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  consent1_next_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_90 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_90',
    text: 'I certify that I have read the informed consent and received the information to contact the investigators if necessary.\n\nClick ‘y’ for YES\nClick ’n’ for NO, and you will EXIT the study',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "questionnaire_start"
  questionnaire_startClock = new util.Clock();
  text_33 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_33',
    text: 'First you’re going to answer a few questions about how much you worry. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PSWQ1"
  PSWQ1Clock = new util.Clock();
  text_36 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_36',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_56 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_56',
    text: 'If I do not have enough time to do everything, I do not worry about it.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_57 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_57',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ2"
  PSWQ2Clock = new util.Clock();
  text_58 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_58',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_59 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_59',
    text: 'My worries overwhelm me.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_60 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_60',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ3"
  PSWQ3Clock = new util.Clock();
  text_61 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_61',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_62 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_62',
    text: 'I do not tend to worry about things.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_63 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_63',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ4"
  PSWQ4Clock = new util.Clock();
  text_64 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_64',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_65 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_65',
    text: 'Many situations make me worry.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_66 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_66',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ5"
  PSWQ5Clock = new util.Clock();
  text_67 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_67',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_68 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_68',
    text: 'I know I should not worry about things, but I just cannot help it.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_69 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_69',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ6"
  PSWQ6Clock = new util.Clock();
  text_76 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_76',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_77 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_77',
    text: 'When I am under pressure I worry a lot.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_78 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_78',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_25 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ7"
  PSWQ7Clock = new util.Clock();
  text_79 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_79',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_80 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_80',
    text: 'I am always worrying about something.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_81 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_81',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_26 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ8"
  PSWQ8Clock = new util.Clock();
  text_82 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_82',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_83 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_83',
    text: 'I find it easy to dismiss worrisome thoughts.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_84 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_84',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_27 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ9"
  PSWQ9Clock = new util.Clock();
  text_85 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_85',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_86 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_86',
    text: 'As soon as I finish one task, I start to worry about everything else I have to do.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_87 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_87',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_28 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ10"
  PSWQ10Clock = new util.Clock();
  text_88 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_88',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_91 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_91',
    text: 'I never worry about anything.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_92 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_92',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_29 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ11"
  PSWQ11Clock = new util.Clock();
  text_93 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_93',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_94 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_94',
    text: 'When there is nothing more I can do about a concern, I do not worry about it any more.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_95 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_95',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_30 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ12"
  PSWQ12Clock = new util.Clock();
  text_96 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_96',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_97 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_97',
    text: 'I have been a worrier all my life.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_98 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_98',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_31 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ13"
  PSWQ13Clock = new util.Clock();
  text_99 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_99',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_100 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_100',
    text: 'I notice that I have been worrying about things.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_101 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_101',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_32 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ14"
  PSWQ14Clock = new util.Clock();
  text_102 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_102',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_103 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_103',
    text: 'Once I start worrying, I cannot stop.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_104 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_104',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_33 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ15"
  PSWQ15Clock = new util.Clock();
  text_105 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_105',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_106 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_106',
    text: 'I worry all the time.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_107 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_107',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_34 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PSWQ16"
  PSWQ16Clock = new util.Clock();
  text_108 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_108',
    text: 'Rate each of the following statements on a scale of 1 (“not at all typical of me”) to 5 (“very typical of me”). Please do not leave any items blank.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_109 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_109',
    text: 'I have been a worrier all my life.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_110 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_110',
    text: '1=Not at all typical - 2 - 3 - 4 - 5=Very typical',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_35 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "q2_instructions"
  q2_instructionsClock = new util.Clock();
  text_155 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_155',
    text: "Now you’re going to answer a few questions about how much you've been feeling. ",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "AM1"
  AM1Clock = new util.Clock();
  text_156 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_156',
    text: 'How much has this happened to you in past two weeks? 1=Not at all, 3=Sometimes, 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_157 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_157',
    text: 'Feel happier or more cheerful than usual.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_158 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_158',
    text: '1=Not at all - 2 - 3 - 4 - 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_41 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AM2"
  AM2Clock = new util.Clock();
  text_159 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_159',
    text: 'How much has this happened to you in past two weeks? 1=Not at all, 3=Sometimes, 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_160 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_160',
    text: 'Feel more self-confident than usual.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_161 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_161',
    text: '1=Not at all - 2 - 3 - 4 - 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_42 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AM3"
  AM3Clock = new util.Clock();
  text_162 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_162',
    text: 'How much has this happened to you in past two weeks? 1=Not at all, 3=Sometimes, 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_163 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_163',
    text: 'Need LESS Sleep than usual.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_164 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_164',
    text: '1=Not at all - 2 - 3 - 4 - 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_43 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AM4"
  AM4Clock = new util.Clock();
  text_165 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_165',
    text: 'How much has this happened to you in past two weeks? 1=Not at all, 3=Sometimes, 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_166 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_166',
    text: 'I talk more than usual.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_167 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_167',
    text: '1=Not at all - 2 - 3 - 4 - 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_44 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AM5"
  AM5Clock = new util.Clock();
  text_168 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_168',
    text: 'How much has this happened to you in past two weeks? 1=Not at all, 3=Sometimes, 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_169 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_169',
    text: 'I talk more than usual.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_170 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_170',
    text: '1=Not at all - 2 - 3 - 4 - 5=All the time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_45 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "q3_instructions"
  q3_instructionsClock = new util.Clock();
  text_171 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_171',
    text: "Answer Yes (with 'y' key) or No (with 'n') key to the following questions",
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "SPQ1"
  SPQ1Clock = new util.Clock();
  text_173 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_173',
    text: 'Have you ever had the sense that some person or force is around you, even though you\ncannot see anyone?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_174 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_174',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_46 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ2"
  SPQ2Clock = new util.Clock();
  text_175 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_175',
    text: 'Are you sometimes sure that other people can tell what you are thinking?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_176 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_176',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_47 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ3"
  SPQ3Clock = new util.Clock();
  text_177 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_177',
    text: 'Have you ever noticed a common event or object that seemed to be a special sign for\nyou?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_178 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_178',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_48 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ4"
  SPQ4Clock = new util.Clock();
  text_179 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_179',
    text: 'Do you often pick up hidden threats or put-downs from what people say or do?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_180 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_180',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_49 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ5"
  SPQ5Clock = new util.Clock();
  text_181 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_181',
    text: 'Do you often pick up hidden threats or put-downs from what people say or do?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_182 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_182',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_50 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ6"
  SPQ6Clock = new util.Clock();
  text_183 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_183',
    text: 'Have you had experiences with astrology, seeing the future, UFOs, ESP, or a sixth\nsense?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_184 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_184',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_51 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ7"
  SPQ7Clock = new util.Clock();
  text_185 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_185',
    text: 'Do you ever suddenly feel distracted by distant sounds that you are not normally aware\nof?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_186 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_186',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_52 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ8"
  SPQ8Clock = new util.Clock();
  text_187 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_187',
    text: 'Do you often have to keep an eye out to stop people from taking advantage of you?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_188 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_188',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_53 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ9"
  SPQ9Clock = new util.Clock();
  text_189 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_189',
    text: 'People sometimes find me aloof and distant.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_190 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_190',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_54 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ10"
  SPQ10Clock = new util.Clock();
  text_191 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_191',
    text: '1 feel I have to be on my guard even with friends.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_192 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_192',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_55 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SQP11"
  SQP11Clock = new util.Clock();
  text_193 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_193',
    text: 'I feel very uncomfortable in social situations involving unfamiliar people.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_194 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_194',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_56 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ12"
  SPQ12Clock = new util.Clock();
  text_195 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_195',
    text: 'Have you found that it is best not to let other people know too much about you?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_196 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_196',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_57 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ13"
  SPQ13Clock = new util.Clock();
  text_197 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_197',
    text: 'I tend to keep in the background on social occasions.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_198 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_198',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_58 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ14"
  SPQ14Clock = new util.Clock();
  text_199 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_199',
    text: 'Do you feel that you are unable to get "close" to people?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_200 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_200',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_59 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ15"
  SPQ15Clock = new util.Clock();
  text_201 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_201',
    text: 'I feel very uneasy talking to people I do not know well.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_202 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_202',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_60 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ16"
  SPQ16Clock = new util.Clock();
  text_203 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_203',
    text: 'I tend to keep my feelings to myself.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_204 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_204',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_61 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ17"
  SPQ17Clock = new util.Clock();
  text_205 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_205',
    text: 'People sometimes comment on my unusual mannerisms and habits.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_206 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_206',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_62 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ18"
  SPQ18Clock = new util.Clock();
  text_207 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_207',
    text: 'Some people think that I am a very bizarre person.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_208 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_208',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_63 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ19"
  SPQ19Clock = new util.Clock();
  text_209 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_209',
    text: 'Some people find me a bit vague and elusive during a conversation.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_210 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_210',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_64 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ20"
  SPQ20Clock = new util.Clock();
  text_211 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_211',
    text: 'I sometimes use words in unusual ways.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_212 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_212',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_65 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ21"
  SPQ21Clock = new util.Clock();
  text_213 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_213',
    text: '1 am an odd, unusual person.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_214 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_214',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_66 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SPQ22"
  SPQ22Clock = new util.Clock();
  text_215 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_215',
    text: 'I find it hard to communicate clearly what I want to say to people.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_216 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_216',
    text: 'y=YES        n=NO',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_67 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "q4_instructions"
  q4_instructionsClock = new util.Clock();
  text_172 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_172',
    text: 'Now you will rate how much you feel several emotions at this moment',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "SS1"
  SS1Clock = new util.Clock();
  text_217 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_217',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_218 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_218',
    text: 'Dissatisfied',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_219 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_219',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_68 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS2"
  SS2Clock = new util.Clock();
  text_220 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_220',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_221 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_221',
    text: 'Alert',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_222 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_222',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_69 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS3"
  SS3Clock = new util.Clock();
  text_223 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_223',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_224 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_224',
    text: 'Depressed',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_225 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_225',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_70 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS4"
  SS4Clock = new util.Clock();
  text_226 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_226',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_227 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_227',
    text: 'Sad',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_228 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_228',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_71 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS5"
  SS5Clock = new util.Clock();
  text_229 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_229',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_230 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_230',
    text: 'Active',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_231 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_231',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_72 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS6"
  SS6Clock = new util.Clock();
  text_232 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_232',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_233 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_233',
    text: 'Impatient',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_234 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_234',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_73 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS7"
  SS7Clock = new util.Clock();
  text_235 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_235',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_236 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_236',
    text: 'Annoyed',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_237 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_237',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_74 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS8"
  SS8Clock = new util.Clock();
  text_238 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_238',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_239 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_239',
    text: 'Angry',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_240 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_240',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_75 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS9"
  SS9Clock = new util.Clock();
  text_241 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_241',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_242 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_242',
    text: 'Irritated',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_243 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_243',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_76 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SS10"
  SS10Clock = new util.Clock();
  text_244 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_244',
    text: 'How much do you feel this emotion now?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.28], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_245 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_245',
    text: 'Grouchy',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_246 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_246',
    text: '1=Not at all - 2 - 3 - 4 - 5=Extremely',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_77 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  // Run 'Begin Experiment' code from code_2
  incorrect_actions = 0;
  cogmap = {"baby_left": "backpack", "baby_right": "bowtie", "toothbrush_left": "car", "toothbrush_right": "backpack", "backpack_left": "lamp", "backpack_right": "zebra", "car_left": "cat", "car_right": "lamp", "bowtie_left": "knight", "bowtie_right": "lamp"};
  cogmap_replanning = {"baby_left": "car", "baby_right": "backpack", "toothbrush_left": "bowtie", "toothbrush_right": "backpack", "hourglass_left": "bending", "hourglass_right": "zebra", "backpack_left": "lamp", "backpack_right": "hourglass", "lamp_left": "zebra", "lamp_right": "knight", "cat_left": "zebra", "cat_right": "hammer", "car_left": "cat", "car_right": "lamp", "bowtie_left": "lamp", "bowtie_right": "lamp"};
  current_image = "images/baby.png";
  current_image2 = "images/backpack.png";
  current_image3 = "images/lamp.png";
  current_image4 = "images/zebra.png";
  alternative_image = "images/car.png";
  
  instruction_test = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_test',
    text: 'The beginning of the task will involve learning associations between images. You will be told to click left or right at a starting image. You will then see which picture you see next. Your goal is to learn how to get from one picture to the next depending on which direction you go — left or right.\n\nIf you fail to click the correct button 5 times, you will be exited from the game and not win any money. Also, be sure NOT TO CLICK ESC on your keyboard, as that will also exit you from the game. \n\nLAST, if you do not get a high enough score on a simple memory test by the end of training, you are at risk of losing half of your money. So pay attention on memory quizzes!\n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.042,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  end_instructions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "second_instructions"
  second_instructionsClock = new util.Clock();
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_22 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_22',
    text: 'Your goal is to learn which new picture you will arrive at after selecting a picture by clicking LEFT or RIGHT on your keyboard.\n\nNOTE: There will be a SECOND phase after this first phase, where you can use what you learned to win even more money!\n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "third_instructions"
  third_instructionsClock = new util.Clock();
  responseleft = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_23 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_23',
    text: 'Remember, your goal is to remember which images come after you choose and the action, LEFT or RIGHT at a starting image. For example, choosing LEFT at a picture of an APPLE may take you to a different image than choosing RIGHT.\n\nTo show you what this looks like, you will do a practice round. You will be tested to see if you remember which images come after the starting image. Good luck! \n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instructions4"
  instructions4Clock = new util.Clock();
  text_153 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_153',
    text: 'If you fail to get 100% on the questions that make sure you understand the ways to get from one picture to the next picture, THE GAME WILL EXIT and you will receive only partial credit for time spent.\n\npay attention during learning so you can win more money! ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice1"
  practice1Clock = new util.Clock();
  image_22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_22', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_40 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_40',
    text: 'Press left',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "practice1_result"
  practice1_resultClock = new util.Clock();
  image_20 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_20', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "next_trial"
  next_trialClock = new util.Clock();
  next_trial_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_trial_text',
    text: 'next trial…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice1_quiz"
  practice1_quizClock = new util.Clock();
  basket_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'basket_2', units : undefined, 
    image : 'basket.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.6), (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fireworks_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fireworks_2', units : undefined, 
    image : 'fireworks.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  tree_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tree_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'A',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.6), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: 'G',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  text_27 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_27',
    text: 'L',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.6, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  practice_answer = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_26 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_26',
    text: 'Which image below did you see after clicking LEFT at the apple image?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "practice1_quizfeedback"
  practice1_quizfeedbackClock = new util.Clock();
  text_30 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_30',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "memory_quiz_instructions"
  memory_quiz_instructionsClock = new util.Clock();
  text_75 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_75',
    text: 'During your learning about how to get from one picture to another, you will be tested on your learning.\n\nEvery so often (30 trials) you will be asked to use what you’ve learned to try to reach an image where money is hiding. Each of these questions has a correct answer, and we will reward you at the end of the study based on how well you did on these questions. \n\nSpecifically, we will pick a total of 5 rounds at random from these rounds where you can earn reward to determine how much money you win\n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_23 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quiz1_i"
  quiz1_iClock = new util.Clock();
  text_43 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_43',
    text: 'Instructions Quiz\n\n1. What is the goal of the picture game?\n\na.to learn the type of picture\n\nb.to learn the meaning of pictures\n\nc.to learn which pictures come after taking actions (left or right) certain pictures\n\nd.to learn how actions you take at a picture give you rewards or punishments',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quiz2_i"
  quiz2_iClock = new util.Clock();
  text_70 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_70',
    text: 'Instructions Quiz\n\n2. Will you be quizzed during a learning phase about how to get to certain images?\n\na. no\n\nb. yes, every trial you will be quizzed\n\nc. yes, every so oftern (30 trials) you will be quizzed\n\nd. yes, but only at the end of training',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quiz3"
  quiz3Clock = new util.Clock();
  text_71 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_71',
    text: 'Instructions Quiz\n\n3. What happens during the memory quiz?\n\na.you must recall how the pictures look\n\nb. you must REMEMBER the action that will take you a starting image to an upcoming image. 5 of these questions picked at random by the computer will add money to your total\n\nc. you must recall images you most likely DO NOT see after taking an action at a starting image\n\nd. FORGET the action that will take you a starting image to an upcoming image. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quiz4"
  quiz4Clock = new util.Clock();
  text_72 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_72',
    text: 'Instructions Quiz\n\n4. After learning you will:\n\na. Be done with the task\n\nb. Use what you learned to plan how to get to certain images\n\nc. Asked to paint an image of what you learned\n\nd. answer many questions about how much you liked the game',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quiz_feedback"
  quiz_feedbackClock = new util.Clock();
  result_q_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'result_q_instr',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "start_learning"
  start_learningClock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'Press SPACE to start learning!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "learn1"
  learn1Clock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "check_incorrect1"
  check_incorrect1Clock = new util.Clock();
  text_incorrect_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_incorrect_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "learn2"
  learn2Clock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "counter_quizzes_round"
  counter_quizzes_roundClock = new util.Clock();
  // Initialize components for Routine "between"
  betweenClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Time for a memory quiz based on what you learned',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "quiz"
  quizClock = new util.Clock();
  target_quiz1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_quiz1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  question_quiz1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_quiz1',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  answer_quiz1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  answer1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.45), (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  answer2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  answer3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  answer4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.45, (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  a1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a1',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  a2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a2',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  a3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a3',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -9.0 
  });
  
  a4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a4',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.45, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "back_to_learn"
  back_to_learnClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'Take a break for 5 seconds before the next round of learning',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "check_incorrect"
  check_incorrectClock = new util.Clock();
  text_incorrect = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_incorrect',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "quiz2"
  quiz2Clock = new util.Clock();
  target_quiz1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_quiz1_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.15], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  question_quiz1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_quiz1_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  answer_quiz1_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  answer1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer1_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.45), (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  answer2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer2_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  answer3_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer3_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  answer4_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer4_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.45, (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  a1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a1_2',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  a2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a2_2',
    text: '2',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  a3_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a3_2',
    text: '3',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -9.0 
  });
  
  a4_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a4_2',
    text: '4',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.45, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "planning_paths"
  planning_pathsClock = new util.Clock();
  text_149 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_149',
    text: 'Plan how to get from either the BABY or TOOTHBRUSH to new images. \n\nPlan how to get from one image to the next image. \n\nREMEMBER: Nothing has changed since you initially learned about how to navigate between pictures at the beginning of the task.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_40 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_49 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_49',
    text: 'Press space to begin',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "forgetting_paths1"
  forgetting_paths1Clock = new util.Clock();
  question_quiz1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_quiz1_3',
    text: 'Plan the 2 actions in your head how to get from the left image to the right image. You have two minutes to plan.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  answer_quiz1_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  answer1_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer1_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.4), 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  answer2_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer2_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  answer3_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer3_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.4, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  a1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a1_3',
    text: '>',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  a2_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a2_3',
    text: '>',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_146 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_146',
    text: 'Click the two actions (a sequence of LEFT and RIGHT) on the keyboard that will get you from the image on the far left to the image on the far right.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.28)], height: 0.055,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "planningpathstraining2"
  planningpathstraining2Clock = new util.Clock();
  question_quiz1_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'question_quiz1_5',
    text: 'Plan the 2 actions in your head how to get from the left image to the right image. You have two minutes to plan.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  answer_quiz1_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  answer1_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer1_5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.4), 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  answer2_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer2_5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  answer3_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'answer3_5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.4, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  a1_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a1_5',
    text: '>',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  a2_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a2_5',
    text: '>',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_152 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_152',
    text: 'Click the two actions (a sequence of LEFT and RIGHT) on the keyboard that will get you from the image on the far left to the image on the far right.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.28)], height: 0.055,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "correct_forget_paths"
  correct_forget_pathsClock = new util.Clock();
  next_trial_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_trial_text_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_151 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_151',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "total_score_planning"
  total_score_planningClock = new util.Clock();
  next_trial_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'next_trial_text_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_150 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_150',
    text: 'Percent correct:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.05], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "break_routine"
  break_routineClock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'Next stage: Planning phase!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instructions_reward"
  instructions_rewardClock = new util.Clock();
  instructions_rewardstage = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_rewardstage',
    text: 'Now it’s time to use what you learned to get rewards. You will play a series of trials that each have 3 decisions. Each decision, you will be shown a long-term BIG reward that you can get to at the 3rd decision. You can plan how to get there based off of what you learned.\n\nThe first choice will always involve choosing whether you start at the picture of the BABY or the picture of the TOOTHBRUSH. After that, you will click either LEFT or RIGHT to try to get to new pictures. \n\nIMPORTANT: You will always have the option to click SPACE to win 100 points. By choosing this option, the computer will take take you to a new image by choosing left or right for you. For example, on the first trial, if you click SPACE, the computer will randomly select either BABY or TOOTHBRUSH for you.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.032,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_46 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_46',
    text: 'Press SPACE to continue ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.32)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "instructions_planning_2"
  instructions_planning_2Clock = new util.Clock();
  text_50 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_50',
    text: 'VERY RARELY, the computer will take you to a location you didn’t want to go.\n\nTry your best to get the most points possible! You can win the most points both by collecting immediate rewards by clicking SPACE and by reaching and winning the long-term goals.\n\nYou will always see your WINNING TOTAL on each screen and your goal is to win the most points to win th most money!\n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_20
  directions_dict = {"baby_left": "images/backpack.png", "baby_right": "images/bowtie.png", "toothbrush_left": "images/car.png", "toothbrush_right": "images/backpack.png", "hourglass_right": "images/hammer.png", "hourglass_left": "images/knight.png", "backpack_left": "images/lamp.png", "backpack_right": "images/hourglass.png", "lamp_left": "images/hammer.png", "lamp_right": "images/bending.png", "cat_left": "images/hammer.png", "cat_right": "images/zebra.png", "car_left": "images/cat.png", "car_right": "images/lamp.png", "bowtie_left": "images/lamp.png", "bowtie_right": "images/lamp.png"};
  incorrect_actions = 0;
  action = "left.png";
  correct_quiz = "p";
  percent_correct = "";
  text_correct = "";
  
  // Initialize components for Routine "instructions_example_trial"
  instructions_example_trialClock = new util.Clock();
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: 'EXAMPLE TRIAL: You are now at the image below. Choose left or right based off of what you learned to get the most points in images listed below!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  R1_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R1_5', units : undefined, 
    image : 'images/knight.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  R2_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2_5', units : undefined, 
    image : 'images/computer.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  rew1_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew1_5',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -4.0 
  });
  
  rew2_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew2_5',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: 'Choose LEFT or RIGHT to try to win points!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.38)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  plan2_response_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  current_image_decision2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'current_image_decision2_2', units : undefined, 
    image : 'images/baby.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.17], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "long_term_reward_instructions"
  long_term_reward_instructionsClock = new util.Clock();
  instructions_rewardstage_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_rewardstage_2',
    text: 'Each planning trial has 3 decisions. You have the chance to win 400 points if you successfully make it to that destination at the 3rd decision. It is always presented on the bottom RIGHT of the 3 decisions, and will NEVER CHANGE across the 3 decisions.\n\nBy contrast, on the bottom LEFT, you can choose to have the computer select which state to go to next, and win 100 points instantly! You will see your total score.\n\nIMPORTANT: MANY TIMES YOU CAN WIN BOTH THE IMMEDIATE REWARD AND THE LONG TERM REWARD!\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.032,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_45 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_45',
    text: 'press SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.32)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "quiz_planning_1"
  quiz_planning_1Clock = new util.Clock();
  text_47 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_47',
    text: 'Planning Quiz\n\n1. What is always the first decision out of the 3 decisions for EVERY planning trial?\n\na. between CAT and TOOTHBRUSH\n\nb. between CAR and TOOTHBRUSH\n\nc. between BABY and TOOTHBRUSH\n\nd. You start at a different point each planning trial',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_21 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quiz_planning_2"
  quiz_planning_2Clock = new util.Clock();
  text_73 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_73',
    text: 'Instructions Quiz\n\n2. What is the long term reward depicted on bottom right?\n\na. It is a reward you can obtain every decision out of the 3 decisions.\n\nb. It is a big reward you can get only at the 3rd decision. Its location will not change across all 3 decisions to allow you to plan how to get there!\n\nc. It is always a reward that you can ONLY get by AVOIDING going for short-term rewards.\n\nd. It is your total amount of winnings in the game.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "quiz_planning_3"
  quiz_planning_3Clock = new util.Clock();
  text_74 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_74',
    text: 'Planning Quiz\n\n3. What happens when you press SPACE ?\n\na. It is the reward you get from memory quizzes during learning\n\nb. You instantly get 100 points but the computer randomly selects LEFT or RIGHT for you, so you don’t know the image you’ll end up at next.\n\nc. It gives you 60 points but PREVENTS you from getting the LONG-term reward. \n\nd. It is the rewards you already got during what you previously learned.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_24 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "see_planning_trials"
  see_planning_trialsClock = new util.Clock();
  text_48 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_48',
    text: 'Now you will see how planning trials look in the real game. These trials will not include the same images you just learned about. However, the same things you learn now in practice will apply to the real planning phase. \n\nPress SPACE to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_planning_new"
  instructions_planning_newClock = new util.Clock();
  text_32 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_32',
    text: 'EXAMPLE Decision 1: Choose SPACE and the computer randomly selects which state you get to.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  R1_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R1_6', units : undefined, 
    image : 'images/computer.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  R2_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2_6', units : undefined, 
    image : 'images/knight.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  rew1_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew1_6',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -4.0 
  });
  
  rew2_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew2_6',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -5.0 
  });
  
  plan2_response_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_34 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_34',
    text: 'Long-Term Reward',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, (- 0.32)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  text_41 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_41',
    text: 'Computer Chooses',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), (- 0.32)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_114 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_114',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.1, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -9.0 
  });
  
  text_128 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_128',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.1), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "planning_2_instructions"
  planning_2_instructionsClock = new util.Clock();
  text_52 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_52',
    text: 'The COMPUTER chose LEFT and now you’re at the PLANET. \nDecision 2: Choose the computer again by clicking SPACE. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.38], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  R1_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R1_9', units : undefined, 
    image : 'images/computer.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  R2_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2_9', units : undefined, 
    image : 'images/knight.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  rew1_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew1_9',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -4.0 
  });
  
  rew2_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew2_9',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_53 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_53',
    text: 'Choose LEFT or RIGHT',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.3)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  plan2_response_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  current_image_decision2_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'current_image_decision2_5', units : undefined, 
    image : 'planet.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.17], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  text_115 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_115',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.1, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -9.0 
  });
  
  text_129 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_129',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "instructions_planning_new3"
  instructions_planning_new3Clock = new util.Clock();
  text_136 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_136',
    text: 'Decision 3: You are at the BASKET. Choose right to get the BIG REWARD at the KNIGHT. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  R1_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R1_11', units : undefined, 
    image : 'images/computer.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.1)], size : [0.1, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  R2_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2_11', units : undefined, 
    image : 'images/knight.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.1)], size : [0.1, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  rew1_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew1_11',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -4.0 
  });
  
  rew2_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew2_11',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -5.0 
  });
  
  plan2_response_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  current_image_decision2_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'current_image_decision2_6', units : undefined, 
    image : 'basket.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.17], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  text_137 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_137',
    text: 'Long-Term Reward',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, (- 0.32)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  text_138 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_138',
    text: 'Short-Term Reward',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), (- 0.32)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -9.0 
  });
  
  text_139 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_139',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.1, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -10.0 
  });
  
  text_140 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_140',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -11.0 
  });
  
  // Initialize components for Routine "practice_planning_outcomes"
  practice_planning_outcomesClock = new util.Clock();
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', units : undefined, 
    image : 'images/knight.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text_141 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_141',
    text: 'You arrived here! ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_142 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_142',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_143 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_143',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.12), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "immediate_rewar_lesson"
  immediate_rewar_lessonClock = new util.Clock();
  text_148 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_148',
    text: 'NOTICE: You were able to avoid planning twice by clicking SPACE to win 200 more points and STILL arrive at the long-term goal of KNIGHT. In the upcoming planning phase, use what you know about how to get to long term goals to determine when it is best to choose yourself or let the COMPUTER choose for you to win more points. Press SPACE to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_39 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "lesson_practice"
  lesson_practiceClock = new util.Clock();
  text_144 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_144',
    text: 'If you do well in upcoming planning trials, you can WIN even more bonus MONEY!\n\nIMPORTANT: when you press SPACE to have the computer choose for you, it will always take you to a new image the way you learned about in the learning phase. After this random choice, you will then be able to try to reach the long term goal image from where the random choice led you to.\n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_37 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "lesson_practice_2"
  lesson_practice_2Clock = new util.Clock();
  text_145 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_145',
    text: 'IMPORTANT: Each big long-term image you can plan to reach has a different amount of ROUTES to get there. For example, one long-term image may have only one route, while another may have many! Use this to choose well and win the most points you can! \n\n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_38 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "start_real_planning"
  start_real_planningClock = new util.Clock();
  text_42 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_42',
    text: 'Starting the actual planning phase. \n\nREMEMBER: You have UNLIMITED time to plan. Try to figure out when it makes sense press SPACE and have the computer choose for you in a way that still makes sure you can get to the BIG REWARD. \n\npress SPACE to start and good luck!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "plan1_info_2"
  plan1_info_2Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Choose LEFT for BABY or RIGHT for TOOTHBRUSH or SPACE. Make this choice by considering how to get the most points at the images shown below.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  R1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R1', units : undefined, 
    image : 'images/computer.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.12)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  R2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.12)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  rew1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew1',
    text: 'SPACE for 100',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.27)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -4.0 
  });
  
  rew2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.27)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Left or Right',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.32)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  plan1_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  babyleft = new visual.ImageStim({
    win : psychoJS.window,
    name : 'babyleft', units : undefined, 
    image : 'images/baby.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.2), 0.2], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  toothbrushright = new visual.ImageStim({
    win : psychoJS.window,
    name : 'toothbrushright', units : undefined, 
    image : 'images/toothbrush.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.2, 0.2], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  text_117 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_117',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -10.0 
  });
  
  text_120 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_120',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.1), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -11.0 
  });
  
  // Initialize components for Routine "plan2_info"
  plan2_infoClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'You are now at the image below. Choose left or right or SPACE based off of what you learned to get the most points in images listed below!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  R1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R1_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  R2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  rew1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew1_2',
    text: 'SPACE for 100',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -4.0 
  });
  
  rew2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew2_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'Left or Right',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.32)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  plan2_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  current_image_decision2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'current_image_decision2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.17], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  text_118 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_118',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -9.0 
  });
  
  text_121 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_121',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.1), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "plan3_info"
  plan3_infoClock = new util.Clock();
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'You are now at the image below. Choose left or right or SPACE based off of what you learned to get the most points in images listed below!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  R1_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R1_3', units : undefined, 
    image : 'images/computer.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.15), (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  R2_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'R2_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.15, (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  rew1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew1_3',
    text: 'SPACE for 100',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.15), (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -4.0 
  });
  
  rew2_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rew2_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.22)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('green'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: 'Left or Right',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.15, (- 0.32)], height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  plan3_response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  current_image_decision3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'current_image_decision3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0.17], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  text_122 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_122',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -9.0 
  });
  
  text_123 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_123',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.1), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "planning4"
  planning4Clock = new util.Clock();
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text_19 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_19',
    text: 'You arrived here! ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_119 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_119',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_131 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_131',
    text: 'Total=',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.12), (- 0.41)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_20',
    text: 'Thanks for your participation! you will have your Prolific credit and bonuses updated in the next couple of weeks.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _consent1_next_allKeys;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent' ---
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('consent.started', globalClock.getTime());
    image_11.setImage('consent1.png');
    consent1_next.keys = undefined;
    consent1_next.rt = undefined;
    _consent1_next_allKeys = [];
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(image_11);
    consentComponents.push(consent1_next);
    consentComponents.push(text_89);
    
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent' ---
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_11* updates
    if (t >= 0.0 && image_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_11.tStart = t;  // (not accounting for frame time here)
      image_11.frameNStart = frameN;  // exact frame index
      
      image_11.setAutoDraw(true);
    }
    
    
    // *consent1_next* updates
    if (t >= 0.0 && consent1_next.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent1_next.tStart = t;  // (not accounting for frame time here)
      consent1_next.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consent1_next.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consent1_next.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consent1_next.clearEvents(); });
    }
    
    if (consent1_next.status === PsychoJS.Status.STARTED) {
      let theseKeys = consent1_next.getKeys({keyList: ['space'], waitRelease: false});
      _consent1_next_allKeys = _consent1_next_allKeys.concat(theseKeys);
      if (_consent1_next_allKeys.length > 0) {
        consent1_next.keys = _consent1_next_allKeys[_consent1_next_allKeys.length - 1].name;  // just the last key pressed
        consent1_next.rt = _consent1_next_allKeys[_consent1_next_allKeys.length - 1].rt;
        consent1_next.duration = _consent1_next_allKeys[_consent1_next_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_89* updates
    if (t >= 0.0 && text_89.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_89.tStart = t;  // (not accounting for frame time here)
      text_89.frameNStart = frameN;  // exact frame index
      
      text_89.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent' ---
    consentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('consent.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(consent1_next.corr, level);
    }
    psychoJS.experiment.addData('consent1_next.keys', consent1_next.keys);
    if (typeof consent1_next.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent1_next.rt', consent1_next.rt);
        psychoJS.experiment.addData('consent1_next.duration', consent1_next.duration);
        routineTimer.reset();
        }
    
    consent1_next.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _consent1_next_2_allKeys;
var consent2Components;
function consent2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent2' ---
    t = 0;
    consent2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('consent2.started', globalClock.getTime());
    image_13.setImage('consent2.png');
    consent1_next_2.keys = undefined;
    consent1_next_2.rt = undefined;
    _consent1_next_2_allKeys = [];
    // keep track of which components have finished
    consent2Components = [];
    consent2Components.push(image_13);
    consent2Components.push(consent1_next_2);
    consent2Components.push(text_90);
    
    consent2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function consent2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent2' ---
    // get current time
    t = consent2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_13* updates
    if (t >= 0.0 && image_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_13.tStart = t;  // (not accounting for frame time here)
      image_13.frameNStart = frameN;  // exact frame index
      
      image_13.setAutoDraw(true);
    }
    
    
    // *consent1_next_2* updates
    if (t >= 0.0 && consent1_next_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent1_next_2.tStart = t;  // (not accounting for frame time here)
      consent1_next_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consent1_next_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consent1_next_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consent1_next_2.clearEvents(); });
    }
    
    if (consent1_next_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = consent1_next_2.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _consent1_next_2_allKeys = _consent1_next_2_allKeys.concat(theseKeys);
      if (_consent1_next_2_allKeys.length > 0) {
        consent1_next_2.keys = _consent1_next_2_allKeys[_consent1_next_2_allKeys.length - 1].name;  // just the last key pressed
        consent1_next_2.rt = _consent1_next_2_allKeys[_consent1_next_2_allKeys.length - 1].rt;
        consent1_next_2.duration = _consent1_next_2_allKeys[_consent1_next_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_90* updates
    if (t >= 0.0 && text_90.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_90.tStart = t;  // (not accounting for frame time here)
      text_90.frameNStart = frameN;  // exact frame index
      
      text_90.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    consent2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consent2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent2' ---
    consent2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('consent2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(consent1_next_2.corr, level);
    }
    psychoJS.experiment.addData('consent1_next_2.keys', consent1_next_2.keys);
    if (typeof consent1_next_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent1_next_2.rt', consent1_next_2.rt);
        psychoJS.experiment.addData('consent1_next_2.duration', consent1_next_2.duration);
        routineTimer.reset();
        }
    
    consent1_next_2.stop();
    // Run 'End Routine' code from code_19
    if ((consent1_next_2.keys === "n")) {
        psychoJS.quit();
    }
    
    // the Routine "consent2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var questionnaire_startComponents;
function questionnaire_startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'questionnaire_start' ---
    t = 0;
    questionnaire_startClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('questionnaire_start.started', globalClock.getTime());
    // keep track of which components have finished
    questionnaire_startComponents = [];
    questionnaire_startComponents.push(text_33);
    
    questionnaire_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function questionnaire_startRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'questionnaire_start' ---
    // get current time
    t = questionnaire_startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_33* updates
    if (t >= 0.0 && text_33.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_33.tStart = t;  // (not accounting for frame time here)
      text_33.frameNStart = frameN;  // exact frame index
      
      text_33.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_33.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_33.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    questionnaire_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function questionnaire_startRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'questionnaire_start' ---
    questionnaire_startComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('questionnaire_start.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var PSWQ1Components;
function PSWQ1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ1' ---
    t = 0;
    PSWQ1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ1.started', globalClock.getTime());
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    PSWQ1Components = [];
    PSWQ1Components.push(text_36);
    PSWQ1Components.push(text_56);
    PSWQ1Components.push(text_57);
    PSWQ1Components.push(key_resp_3);
    
    PSWQ1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ1' ---
    // get current time
    t = PSWQ1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_36* updates
    if (t >= 0.0 && text_36.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_36.tStart = t;  // (not accounting for frame time here)
      text_36.frameNStart = frameN;  // exact frame index
      
      text_36.setAutoDraw(true);
    }
    
    
    // *text_56* updates
    if (t >= 0.0 && text_56.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_56.tStart = t;  // (not accounting for frame time here)
      text_56.frameNStart = frameN;  // exact frame index
      
      text_56.setAutoDraw(true);
    }
    
    
    // *text_57* updates
    if (t >= 0.0 && text_57.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_57.tStart = t;  // (not accounting for frame time here)
      text_57.frameNStart = frameN;  // exact frame index
      
      text_57.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ1' ---
    PSWQ1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "PSWQ1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_13_allKeys;
var PSWQ2Components;
function PSWQ2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ2' ---
    t = 0;
    PSWQ2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ2.started', globalClock.getTime());
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    // keep track of which components have finished
    PSWQ2Components = [];
    PSWQ2Components.push(text_58);
    PSWQ2Components.push(text_59);
    PSWQ2Components.push(text_60);
    PSWQ2Components.push(key_resp_13);
    
    PSWQ2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ2' ---
    // get current time
    t = PSWQ2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_58* updates
    if (t >= 0.0 && text_58.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_58.tStart = t;  // (not accounting for frame time here)
      text_58.frameNStart = frameN;  // exact frame index
      
      text_58.setAutoDraw(true);
    }
    
    
    // *text_59* updates
    if (t >= 0.0 && text_59.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_59.tStart = t;  // (not accounting for frame time here)
      text_59.frameNStart = frameN;  // exact frame index
      
      text_59.setAutoDraw(true);
    }
    
    
    // *text_60* updates
    if (t >= 0.0 && text_60.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_60.tStart = t;  // (not accounting for frame time here)
      text_60.frameNStart = frameN;  // exact frame index
      
      text_60.setAutoDraw(true);
    }
    
    
    // *key_resp_13* updates
    if (t >= 0.0 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }
    
    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        key_resp_13.duration = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ2' ---
    PSWQ2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_13.corr, level);
    }
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        psychoJS.experiment.addData('key_resp_13.duration', key_resp_13.duration);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "PSWQ2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_14_allKeys;
var PSWQ3Components;
function PSWQ3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ3' ---
    t = 0;
    PSWQ3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ3.started', globalClock.getTime());
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    // keep track of which components have finished
    PSWQ3Components = [];
    PSWQ3Components.push(text_61);
    PSWQ3Components.push(text_62);
    PSWQ3Components.push(text_63);
    PSWQ3Components.push(key_resp_14);
    
    PSWQ3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ3' ---
    // get current time
    t = PSWQ3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_61* updates
    if (t >= 0.0 && text_61.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_61.tStart = t;  // (not accounting for frame time here)
      text_61.frameNStart = frameN;  // exact frame index
      
      text_61.setAutoDraw(true);
    }
    
    
    // *text_62* updates
    if (t >= 0.0 && text_62.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_62.tStart = t;  // (not accounting for frame time here)
      text_62.frameNStart = frameN;  // exact frame index
      
      text_62.setAutoDraw(true);
    }
    
    
    // *text_63* updates
    if (t >= 0.0 && text_63.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_63.tStart = t;  // (not accounting for frame time here)
      text_63.frameNStart = frameN;  // exact frame index
      
      text_63.setAutoDraw(true);
    }
    
    
    // *key_resp_14* updates
    if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }
    
    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        key_resp_14.duration = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ3' ---
    PSWQ3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_14.corr, level);
    }
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        psychoJS.experiment.addData('key_resp_14.duration', key_resp_14.duration);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "PSWQ3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_15_allKeys;
var PSWQ4Components;
function PSWQ4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ4' ---
    t = 0;
    PSWQ4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ4.started', globalClock.getTime());
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    // keep track of which components have finished
    PSWQ4Components = [];
    PSWQ4Components.push(text_64);
    PSWQ4Components.push(text_65);
    PSWQ4Components.push(text_66);
    PSWQ4Components.push(key_resp_15);
    
    PSWQ4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ4' ---
    // get current time
    t = PSWQ4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_64* updates
    if (t >= 0.0 && text_64.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_64.tStart = t;  // (not accounting for frame time here)
      text_64.frameNStart = frameN;  // exact frame index
      
      text_64.setAutoDraw(true);
    }
    
    
    // *text_65* updates
    if (t >= 0.0 && text_65.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_65.tStart = t;  // (not accounting for frame time here)
      text_65.frameNStart = frameN;  // exact frame index
      
      text_65.setAutoDraw(true);
    }
    
    
    // *text_66* updates
    if (t >= 0.0 && text_66.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_66.tStart = t;  // (not accounting for frame time here)
      text_66.frameNStart = frameN;  // exact frame index
      
      text_66.setAutoDraw(true);
    }
    
    
    // *key_resp_15* updates
    if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }
    
    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        key_resp_15.duration = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ4' ---
    PSWQ4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_15.corr, level);
    }
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        psychoJS.experiment.addData('key_resp_15.duration', key_resp_15.duration);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "PSWQ4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_16_allKeys;
var PSWQ5Components;
function PSWQ5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ5' ---
    t = 0;
    PSWQ5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ5.started', globalClock.getTime());
    key_resp_16.keys = undefined;
    key_resp_16.rt = undefined;
    _key_resp_16_allKeys = [];
    // keep track of which components have finished
    PSWQ5Components = [];
    PSWQ5Components.push(text_67);
    PSWQ5Components.push(text_68);
    PSWQ5Components.push(text_69);
    PSWQ5Components.push(key_resp_16);
    
    PSWQ5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ5' ---
    // get current time
    t = PSWQ5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_67* updates
    if (t >= 0.0 && text_67.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_67.tStart = t;  // (not accounting for frame time here)
      text_67.frameNStart = frameN;  // exact frame index
      
      text_67.setAutoDraw(true);
    }
    
    
    // *text_68* updates
    if (t >= 0.0 && text_68.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_68.tStart = t;  // (not accounting for frame time here)
      text_68.frameNStart = frameN;  // exact frame index
      
      text_68.setAutoDraw(true);
    }
    
    
    // *text_69* updates
    if (t >= 0.0 && text_69.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_69.tStart = t;  // (not accounting for frame time here)
      text_69.frameNStart = frameN;  // exact frame index
      
      text_69.setAutoDraw(true);
    }
    
    
    // *key_resp_16* updates
    if (t >= 0.0 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_16.tStart = t;  // (not accounting for frame time here)
      key_resp_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
    }
    
    if (key_resp_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_16.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_16_allKeys = _key_resp_16_allKeys.concat(theseKeys);
      if (_key_resp_16_allKeys.length > 0) {
        key_resp_16.keys = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].name;  // just the last key pressed
        key_resp_16.rt = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].rt;
        key_resp_16.duration = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ5' ---
    PSWQ5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_16.corr, level);
    }
    psychoJS.experiment.addData('key_resp_16.keys', key_resp_16.keys);
    if (typeof key_resp_16.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_16.rt', key_resp_16.rt);
        psychoJS.experiment.addData('key_resp_16.duration', key_resp_16.duration);
        routineTimer.reset();
        }
    
    key_resp_16.stop();
    // the Routine "PSWQ5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_25_allKeys;
var PSWQ6Components;
function PSWQ6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ6' ---
    t = 0;
    PSWQ6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ6.started', globalClock.getTime());
    key_resp_25.keys = undefined;
    key_resp_25.rt = undefined;
    _key_resp_25_allKeys = [];
    // keep track of which components have finished
    PSWQ6Components = [];
    PSWQ6Components.push(text_76);
    PSWQ6Components.push(text_77);
    PSWQ6Components.push(text_78);
    PSWQ6Components.push(key_resp_25);
    
    PSWQ6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ6' ---
    // get current time
    t = PSWQ6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_76* updates
    if (t >= 0.0 && text_76.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_76.tStart = t;  // (not accounting for frame time here)
      text_76.frameNStart = frameN;  // exact frame index
      
      text_76.setAutoDraw(true);
    }
    
    
    // *text_77* updates
    if (t >= 0.0 && text_77.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_77.tStart = t;  // (not accounting for frame time here)
      text_77.frameNStart = frameN;  // exact frame index
      
      text_77.setAutoDraw(true);
    }
    
    
    // *text_78* updates
    if (t >= 0.0 && text_78.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_78.tStart = t;  // (not accounting for frame time here)
      text_78.frameNStart = frameN;  // exact frame index
      
      text_78.setAutoDraw(true);
    }
    
    
    // *key_resp_25* updates
    if (t >= 0.0 && key_resp_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_25.tStart = t;  // (not accounting for frame time here)
      key_resp_25.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_25.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_25.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_25.clearEvents(); });
    }
    
    if (key_resp_25.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_25.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_25_allKeys = _key_resp_25_allKeys.concat(theseKeys);
      if (_key_resp_25_allKeys.length > 0) {
        key_resp_25.keys = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].name;  // just the last key pressed
        key_resp_25.rt = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].rt;
        key_resp_25.duration = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ6' ---
    PSWQ6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ6.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_25.corr, level);
    }
    psychoJS.experiment.addData('key_resp_25.keys', key_resp_25.keys);
    if (typeof key_resp_25.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_25.rt', key_resp_25.rt);
        psychoJS.experiment.addData('key_resp_25.duration', key_resp_25.duration);
        routineTimer.reset();
        }
    
    key_resp_25.stop();
    // the Routine "PSWQ6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_26_allKeys;
var PSWQ7Components;
function PSWQ7RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ7' ---
    t = 0;
    PSWQ7Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ7.started', globalClock.getTime());
    key_resp_26.keys = undefined;
    key_resp_26.rt = undefined;
    _key_resp_26_allKeys = [];
    // keep track of which components have finished
    PSWQ7Components = [];
    PSWQ7Components.push(text_79);
    PSWQ7Components.push(text_80);
    PSWQ7Components.push(text_81);
    PSWQ7Components.push(key_resp_26);
    
    PSWQ7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ7RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ7' ---
    // get current time
    t = PSWQ7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_79* updates
    if (t >= 0.0 && text_79.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_79.tStart = t;  // (not accounting for frame time here)
      text_79.frameNStart = frameN;  // exact frame index
      
      text_79.setAutoDraw(true);
    }
    
    
    // *text_80* updates
    if (t >= 0.0 && text_80.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_80.tStart = t;  // (not accounting for frame time here)
      text_80.frameNStart = frameN;  // exact frame index
      
      text_80.setAutoDraw(true);
    }
    
    
    // *text_81* updates
    if (t >= 0.0 && text_81.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_81.tStart = t;  // (not accounting for frame time here)
      text_81.frameNStart = frameN;  // exact frame index
      
      text_81.setAutoDraw(true);
    }
    
    
    // *key_resp_26* updates
    if (t >= 0.0 && key_resp_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_26.tStart = t;  // (not accounting for frame time here)
      key_resp_26.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_26.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_26.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_26.clearEvents(); });
    }
    
    if (key_resp_26.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_26.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_26_allKeys = _key_resp_26_allKeys.concat(theseKeys);
      if (_key_resp_26_allKeys.length > 0) {
        key_resp_26.keys = _key_resp_26_allKeys[_key_resp_26_allKeys.length - 1].name;  // just the last key pressed
        key_resp_26.rt = _key_resp_26_allKeys[_key_resp_26_allKeys.length - 1].rt;
        key_resp_26.duration = _key_resp_26_allKeys[_key_resp_26_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ7RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ7' ---
    PSWQ7Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ7.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_26.corr, level);
    }
    psychoJS.experiment.addData('key_resp_26.keys', key_resp_26.keys);
    if (typeof key_resp_26.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_26.rt', key_resp_26.rt);
        psychoJS.experiment.addData('key_resp_26.duration', key_resp_26.duration);
        routineTimer.reset();
        }
    
    key_resp_26.stop();
    // the Routine "PSWQ7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_27_allKeys;
var PSWQ8Components;
function PSWQ8RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ8' ---
    t = 0;
    PSWQ8Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ8.started', globalClock.getTime());
    key_resp_27.keys = undefined;
    key_resp_27.rt = undefined;
    _key_resp_27_allKeys = [];
    // keep track of which components have finished
    PSWQ8Components = [];
    PSWQ8Components.push(text_82);
    PSWQ8Components.push(text_83);
    PSWQ8Components.push(text_84);
    PSWQ8Components.push(key_resp_27);
    
    PSWQ8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ8RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ8' ---
    // get current time
    t = PSWQ8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_82* updates
    if (t >= 0.0 && text_82.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_82.tStart = t;  // (not accounting for frame time here)
      text_82.frameNStart = frameN;  // exact frame index
      
      text_82.setAutoDraw(true);
    }
    
    
    // *text_83* updates
    if (t >= 0.0 && text_83.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_83.tStart = t;  // (not accounting for frame time here)
      text_83.frameNStart = frameN;  // exact frame index
      
      text_83.setAutoDraw(true);
    }
    
    
    // *text_84* updates
    if (t >= 0.0 && text_84.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_84.tStart = t;  // (not accounting for frame time here)
      text_84.frameNStart = frameN;  // exact frame index
      
      text_84.setAutoDraw(true);
    }
    
    
    // *key_resp_27* updates
    if (t >= 0.0 && key_resp_27.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_27.tStart = t;  // (not accounting for frame time here)
      key_resp_27.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_27.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_27.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_27.clearEvents(); });
    }
    
    if (key_resp_27.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_27.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_27_allKeys = _key_resp_27_allKeys.concat(theseKeys);
      if (_key_resp_27_allKeys.length > 0) {
        key_resp_27.keys = _key_resp_27_allKeys[_key_resp_27_allKeys.length - 1].name;  // just the last key pressed
        key_resp_27.rt = _key_resp_27_allKeys[_key_resp_27_allKeys.length - 1].rt;
        key_resp_27.duration = _key_resp_27_allKeys[_key_resp_27_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ8RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ8' ---
    PSWQ8Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ8.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_27.corr, level);
    }
    psychoJS.experiment.addData('key_resp_27.keys', key_resp_27.keys);
    if (typeof key_resp_27.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_27.rt', key_resp_27.rt);
        psychoJS.experiment.addData('key_resp_27.duration', key_resp_27.duration);
        routineTimer.reset();
        }
    
    key_resp_27.stop();
    // the Routine "PSWQ8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_28_allKeys;
var PSWQ9Components;
function PSWQ9RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ9' ---
    t = 0;
    PSWQ9Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ9.started', globalClock.getTime());
    key_resp_28.keys = undefined;
    key_resp_28.rt = undefined;
    _key_resp_28_allKeys = [];
    // keep track of which components have finished
    PSWQ9Components = [];
    PSWQ9Components.push(text_85);
    PSWQ9Components.push(text_86);
    PSWQ9Components.push(text_87);
    PSWQ9Components.push(key_resp_28);
    
    PSWQ9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ9RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ9' ---
    // get current time
    t = PSWQ9Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_85* updates
    if (t >= 0.0 && text_85.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_85.tStart = t;  // (not accounting for frame time here)
      text_85.frameNStart = frameN;  // exact frame index
      
      text_85.setAutoDraw(true);
    }
    
    
    // *text_86* updates
    if (t >= 0.0 && text_86.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_86.tStart = t;  // (not accounting for frame time here)
      text_86.frameNStart = frameN;  // exact frame index
      
      text_86.setAutoDraw(true);
    }
    
    
    // *text_87* updates
    if (t >= 0.0 && text_87.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_87.tStart = t;  // (not accounting for frame time here)
      text_87.frameNStart = frameN;  // exact frame index
      
      text_87.setAutoDraw(true);
    }
    
    
    // *key_resp_28* updates
    if (t >= 0.0 && key_resp_28.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_28.tStart = t;  // (not accounting for frame time here)
      key_resp_28.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_28.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_28.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_28.clearEvents(); });
    }
    
    if (key_resp_28.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_28.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_28_allKeys = _key_resp_28_allKeys.concat(theseKeys);
      if (_key_resp_28_allKeys.length > 0) {
        key_resp_28.keys = _key_resp_28_allKeys[_key_resp_28_allKeys.length - 1].name;  // just the last key pressed
        key_resp_28.rt = _key_resp_28_allKeys[_key_resp_28_allKeys.length - 1].rt;
        key_resp_28.duration = _key_resp_28_allKeys[_key_resp_28_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ9RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ9' ---
    PSWQ9Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ9.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_28.corr, level);
    }
    psychoJS.experiment.addData('key_resp_28.keys', key_resp_28.keys);
    if (typeof key_resp_28.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_28.rt', key_resp_28.rt);
        psychoJS.experiment.addData('key_resp_28.duration', key_resp_28.duration);
        routineTimer.reset();
        }
    
    key_resp_28.stop();
    // the Routine "PSWQ9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_29_allKeys;
var PSWQ10Components;
function PSWQ10RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ10' ---
    t = 0;
    PSWQ10Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ10.started', globalClock.getTime());
    key_resp_29.keys = undefined;
    key_resp_29.rt = undefined;
    _key_resp_29_allKeys = [];
    // keep track of which components have finished
    PSWQ10Components = [];
    PSWQ10Components.push(text_88);
    PSWQ10Components.push(text_91);
    PSWQ10Components.push(text_92);
    PSWQ10Components.push(key_resp_29);
    
    PSWQ10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ10RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ10' ---
    // get current time
    t = PSWQ10Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_88* updates
    if (t >= 0.0 && text_88.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_88.tStart = t;  // (not accounting for frame time here)
      text_88.frameNStart = frameN;  // exact frame index
      
      text_88.setAutoDraw(true);
    }
    
    
    // *text_91* updates
    if (t >= 0.0 && text_91.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_91.tStart = t;  // (not accounting for frame time here)
      text_91.frameNStart = frameN;  // exact frame index
      
      text_91.setAutoDraw(true);
    }
    
    
    // *text_92* updates
    if (t >= 0.0 && text_92.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_92.tStart = t;  // (not accounting for frame time here)
      text_92.frameNStart = frameN;  // exact frame index
      
      text_92.setAutoDraw(true);
    }
    
    
    // *key_resp_29* updates
    if (t >= 0.0 && key_resp_29.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_29.tStart = t;  // (not accounting for frame time here)
      key_resp_29.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_29.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_29.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_29.clearEvents(); });
    }
    
    if (key_resp_29.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_29.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_29_allKeys = _key_resp_29_allKeys.concat(theseKeys);
      if (_key_resp_29_allKeys.length > 0) {
        key_resp_29.keys = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].name;  // just the last key pressed
        key_resp_29.rt = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].rt;
        key_resp_29.duration = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ10RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ10' ---
    PSWQ10Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ10.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_29.corr, level);
    }
    psychoJS.experiment.addData('key_resp_29.keys', key_resp_29.keys);
    if (typeof key_resp_29.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_29.rt', key_resp_29.rt);
        psychoJS.experiment.addData('key_resp_29.duration', key_resp_29.duration);
        routineTimer.reset();
        }
    
    key_resp_29.stop();
    // the Routine "PSWQ10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_30_allKeys;
var PSWQ11Components;
function PSWQ11RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ11' ---
    t = 0;
    PSWQ11Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ11.started', globalClock.getTime());
    key_resp_30.keys = undefined;
    key_resp_30.rt = undefined;
    _key_resp_30_allKeys = [];
    // keep track of which components have finished
    PSWQ11Components = [];
    PSWQ11Components.push(text_93);
    PSWQ11Components.push(text_94);
    PSWQ11Components.push(text_95);
    PSWQ11Components.push(key_resp_30);
    
    PSWQ11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ11RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ11' ---
    // get current time
    t = PSWQ11Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_93* updates
    if (t >= 0.0 && text_93.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_93.tStart = t;  // (not accounting for frame time here)
      text_93.frameNStart = frameN;  // exact frame index
      
      text_93.setAutoDraw(true);
    }
    
    
    // *text_94* updates
    if (t >= 0.0 && text_94.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_94.tStart = t;  // (not accounting for frame time here)
      text_94.frameNStart = frameN;  // exact frame index
      
      text_94.setAutoDraw(true);
    }
    
    
    // *text_95* updates
    if (t >= 0.0 && text_95.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_95.tStart = t;  // (not accounting for frame time here)
      text_95.frameNStart = frameN;  // exact frame index
      
      text_95.setAutoDraw(true);
    }
    
    
    // *key_resp_30* updates
    if (t >= 0.0 && key_resp_30.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_30.tStart = t;  // (not accounting for frame time here)
      key_resp_30.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_30.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_30.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_30.clearEvents(); });
    }
    
    if (key_resp_30.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_30.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_30_allKeys = _key_resp_30_allKeys.concat(theseKeys);
      if (_key_resp_30_allKeys.length > 0) {
        key_resp_30.keys = _key_resp_30_allKeys[_key_resp_30_allKeys.length - 1].name;  // just the last key pressed
        key_resp_30.rt = _key_resp_30_allKeys[_key_resp_30_allKeys.length - 1].rt;
        key_resp_30.duration = _key_resp_30_allKeys[_key_resp_30_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ11RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ11' ---
    PSWQ11Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ11.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_30.corr, level);
    }
    psychoJS.experiment.addData('key_resp_30.keys', key_resp_30.keys);
    if (typeof key_resp_30.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_30.rt', key_resp_30.rt);
        psychoJS.experiment.addData('key_resp_30.duration', key_resp_30.duration);
        routineTimer.reset();
        }
    
    key_resp_30.stop();
    // the Routine "PSWQ11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_31_allKeys;
var PSWQ12Components;
function PSWQ12RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ12' ---
    t = 0;
    PSWQ12Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ12.started', globalClock.getTime());
    key_resp_31.keys = undefined;
    key_resp_31.rt = undefined;
    _key_resp_31_allKeys = [];
    // keep track of which components have finished
    PSWQ12Components = [];
    PSWQ12Components.push(text_96);
    PSWQ12Components.push(text_97);
    PSWQ12Components.push(text_98);
    PSWQ12Components.push(key_resp_31);
    
    PSWQ12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ12RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ12' ---
    // get current time
    t = PSWQ12Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_96* updates
    if (t >= 0.0 && text_96.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_96.tStart = t;  // (not accounting for frame time here)
      text_96.frameNStart = frameN;  // exact frame index
      
      text_96.setAutoDraw(true);
    }
    
    
    // *text_97* updates
    if (t >= 0.0 && text_97.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_97.tStart = t;  // (not accounting for frame time here)
      text_97.frameNStart = frameN;  // exact frame index
      
      text_97.setAutoDraw(true);
    }
    
    
    // *text_98* updates
    if (t >= 0.0 && text_98.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_98.tStart = t;  // (not accounting for frame time here)
      text_98.frameNStart = frameN;  // exact frame index
      
      text_98.setAutoDraw(true);
    }
    
    
    // *key_resp_31* updates
    if (t >= 0.0 && key_resp_31.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_31.tStart = t;  // (not accounting for frame time here)
      key_resp_31.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_31.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_31.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_31.clearEvents(); });
    }
    
    if (key_resp_31.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_31.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_31_allKeys = _key_resp_31_allKeys.concat(theseKeys);
      if (_key_resp_31_allKeys.length > 0) {
        key_resp_31.keys = _key_resp_31_allKeys[_key_resp_31_allKeys.length - 1].name;  // just the last key pressed
        key_resp_31.rt = _key_resp_31_allKeys[_key_resp_31_allKeys.length - 1].rt;
        key_resp_31.duration = _key_resp_31_allKeys[_key_resp_31_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ12RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ12' ---
    PSWQ12Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ12.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_31.corr, level);
    }
    psychoJS.experiment.addData('key_resp_31.keys', key_resp_31.keys);
    if (typeof key_resp_31.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_31.rt', key_resp_31.rt);
        psychoJS.experiment.addData('key_resp_31.duration', key_resp_31.duration);
        routineTimer.reset();
        }
    
    key_resp_31.stop();
    // the Routine "PSWQ12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_32_allKeys;
var PSWQ13Components;
function PSWQ13RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ13' ---
    t = 0;
    PSWQ13Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ13.started', globalClock.getTime());
    key_resp_32.keys = undefined;
    key_resp_32.rt = undefined;
    _key_resp_32_allKeys = [];
    // keep track of which components have finished
    PSWQ13Components = [];
    PSWQ13Components.push(text_99);
    PSWQ13Components.push(text_100);
    PSWQ13Components.push(text_101);
    PSWQ13Components.push(key_resp_32);
    
    PSWQ13Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ13RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ13' ---
    // get current time
    t = PSWQ13Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_99* updates
    if (t >= 0.0 && text_99.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_99.tStart = t;  // (not accounting for frame time here)
      text_99.frameNStart = frameN;  // exact frame index
      
      text_99.setAutoDraw(true);
    }
    
    
    // *text_100* updates
    if (t >= 0.0 && text_100.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_100.tStart = t;  // (not accounting for frame time here)
      text_100.frameNStart = frameN;  // exact frame index
      
      text_100.setAutoDraw(true);
    }
    
    
    // *text_101* updates
    if (t >= 0.0 && text_101.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_101.tStart = t;  // (not accounting for frame time here)
      text_101.frameNStart = frameN;  // exact frame index
      
      text_101.setAutoDraw(true);
    }
    
    
    // *key_resp_32* updates
    if (t >= 0.0 && key_resp_32.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_32.tStart = t;  // (not accounting for frame time here)
      key_resp_32.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_32.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_32.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_32.clearEvents(); });
    }
    
    if (key_resp_32.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_32.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_32_allKeys = _key_resp_32_allKeys.concat(theseKeys);
      if (_key_resp_32_allKeys.length > 0) {
        key_resp_32.keys = _key_resp_32_allKeys[_key_resp_32_allKeys.length - 1].name;  // just the last key pressed
        key_resp_32.rt = _key_resp_32_allKeys[_key_resp_32_allKeys.length - 1].rt;
        key_resp_32.duration = _key_resp_32_allKeys[_key_resp_32_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ13Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ13RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ13' ---
    PSWQ13Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ13.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_32.corr, level);
    }
    psychoJS.experiment.addData('key_resp_32.keys', key_resp_32.keys);
    if (typeof key_resp_32.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_32.rt', key_resp_32.rt);
        psychoJS.experiment.addData('key_resp_32.duration', key_resp_32.duration);
        routineTimer.reset();
        }
    
    key_resp_32.stop();
    // the Routine "PSWQ13" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_33_allKeys;
var PSWQ14Components;
function PSWQ14RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ14' ---
    t = 0;
    PSWQ14Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ14.started', globalClock.getTime());
    key_resp_33.keys = undefined;
    key_resp_33.rt = undefined;
    _key_resp_33_allKeys = [];
    // keep track of which components have finished
    PSWQ14Components = [];
    PSWQ14Components.push(text_102);
    PSWQ14Components.push(text_103);
    PSWQ14Components.push(text_104);
    PSWQ14Components.push(key_resp_33);
    
    PSWQ14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ14RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ14' ---
    // get current time
    t = PSWQ14Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_102* updates
    if (t >= 0.0 && text_102.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_102.tStart = t;  // (not accounting for frame time here)
      text_102.frameNStart = frameN;  // exact frame index
      
      text_102.setAutoDraw(true);
    }
    
    
    // *text_103* updates
    if (t >= 0.0 && text_103.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_103.tStart = t;  // (not accounting for frame time here)
      text_103.frameNStart = frameN;  // exact frame index
      
      text_103.setAutoDraw(true);
    }
    
    
    // *text_104* updates
    if (t >= 0.0 && text_104.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_104.tStart = t;  // (not accounting for frame time here)
      text_104.frameNStart = frameN;  // exact frame index
      
      text_104.setAutoDraw(true);
    }
    
    
    // *key_resp_33* updates
    if (t >= 0.0 && key_resp_33.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_33.tStart = t;  // (not accounting for frame time here)
      key_resp_33.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_33.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_33.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_33.clearEvents(); });
    }
    
    if (key_resp_33.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_33.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_33_allKeys = _key_resp_33_allKeys.concat(theseKeys);
      if (_key_resp_33_allKeys.length > 0) {
        key_resp_33.keys = _key_resp_33_allKeys[_key_resp_33_allKeys.length - 1].name;  // just the last key pressed
        key_resp_33.rt = _key_resp_33_allKeys[_key_resp_33_allKeys.length - 1].rt;
        key_resp_33.duration = _key_resp_33_allKeys[_key_resp_33_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ14RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ14' ---
    PSWQ14Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ14.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_33.corr, level);
    }
    psychoJS.experiment.addData('key_resp_33.keys', key_resp_33.keys);
    if (typeof key_resp_33.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_33.rt', key_resp_33.rt);
        psychoJS.experiment.addData('key_resp_33.duration', key_resp_33.duration);
        routineTimer.reset();
        }
    
    key_resp_33.stop();
    // the Routine "PSWQ14" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_34_allKeys;
var PSWQ15Components;
function PSWQ15RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ15' ---
    t = 0;
    PSWQ15Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ15.started', globalClock.getTime());
    key_resp_34.keys = undefined;
    key_resp_34.rt = undefined;
    _key_resp_34_allKeys = [];
    // keep track of which components have finished
    PSWQ15Components = [];
    PSWQ15Components.push(text_105);
    PSWQ15Components.push(text_106);
    PSWQ15Components.push(text_107);
    PSWQ15Components.push(key_resp_34);
    
    PSWQ15Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ15RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ15' ---
    // get current time
    t = PSWQ15Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_105* updates
    if (t >= 0.0 && text_105.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_105.tStart = t;  // (not accounting for frame time here)
      text_105.frameNStart = frameN;  // exact frame index
      
      text_105.setAutoDraw(true);
    }
    
    
    // *text_106* updates
    if (t >= 0.0 && text_106.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_106.tStart = t;  // (not accounting for frame time here)
      text_106.frameNStart = frameN;  // exact frame index
      
      text_106.setAutoDraw(true);
    }
    
    
    // *text_107* updates
    if (t >= 0.0 && text_107.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_107.tStart = t;  // (not accounting for frame time here)
      text_107.frameNStart = frameN;  // exact frame index
      
      text_107.setAutoDraw(true);
    }
    
    
    // *key_resp_34* updates
    if (t >= 0.0 && key_resp_34.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_34.tStart = t;  // (not accounting for frame time here)
      key_resp_34.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_34.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_34.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_34.clearEvents(); });
    }
    
    if (key_resp_34.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_34.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_34_allKeys = _key_resp_34_allKeys.concat(theseKeys);
      if (_key_resp_34_allKeys.length > 0) {
        key_resp_34.keys = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].name;  // just the last key pressed
        key_resp_34.rt = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].rt;
        key_resp_34.duration = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ15Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ15RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ15' ---
    PSWQ15Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ15.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_34.corr, level);
    }
    psychoJS.experiment.addData('key_resp_34.keys', key_resp_34.keys);
    if (typeof key_resp_34.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_34.rt', key_resp_34.rt);
        psychoJS.experiment.addData('key_resp_34.duration', key_resp_34.duration);
        routineTimer.reset();
        }
    
    key_resp_34.stop();
    // the Routine "PSWQ15" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_35_allKeys;
var PSWQ16Components;
function PSWQ16RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PSWQ16' ---
    t = 0;
    PSWQ16Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('PSWQ16.started', globalClock.getTime());
    key_resp_35.keys = undefined;
    key_resp_35.rt = undefined;
    _key_resp_35_allKeys = [];
    // keep track of which components have finished
    PSWQ16Components = [];
    PSWQ16Components.push(text_108);
    PSWQ16Components.push(text_109);
    PSWQ16Components.push(text_110);
    PSWQ16Components.push(key_resp_35);
    
    PSWQ16Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PSWQ16RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PSWQ16' ---
    // get current time
    t = PSWQ16Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_108* updates
    if (t >= 0.0 && text_108.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_108.tStart = t;  // (not accounting for frame time here)
      text_108.frameNStart = frameN;  // exact frame index
      
      text_108.setAutoDraw(true);
    }
    
    
    // *text_109* updates
    if (t >= 0.0 && text_109.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_109.tStart = t;  // (not accounting for frame time here)
      text_109.frameNStart = frameN;  // exact frame index
      
      text_109.setAutoDraw(true);
    }
    
    
    // *text_110* updates
    if (t >= 0.0 && text_110.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_110.tStart = t;  // (not accounting for frame time here)
      text_110.frameNStart = frameN;  // exact frame index
      
      text_110.setAutoDraw(true);
    }
    
    
    // *key_resp_35* updates
    if (t >= 0.0 && key_resp_35.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_35.tStart = t;  // (not accounting for frame time here)
      key_resp_35.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_35.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_35.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_35.clearEvents(); });
    }
    
    if (key_resp_35.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_35.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_35_allKeys = _key_resp_35_allKeys.concat(theseKeys);
      if (_key_resp_35_allKeys.length > 0) {
        key_resp_35.keys = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].name;  // just the last key pressed
        key_resp_35.rt = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].rt;
        key_resp_35.duration = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    PSWQ16Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PSWQ16RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PSWQ16' ---
    PSWQ16Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('PSWQ16.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_35.corr, level);
    }
    psychoJS.experiment.addData('key_resp_35.keys', key_resp_35.keys);
    if (typeof key_resp_35.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_35.rt', key_resp_35.rt);
        psychoJS.experiment.addData('key_resp_35.duration', key_resp_35.duration);
        routineTimer.reset();
        }
    
    key_resp_35.stop();
    // the Routine "PSWQ16" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var q2_instructionsComponents;
function q2_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'q2_instructions' ---
    t = 0;
    q2_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('q2_instructions.started', globalClock.getTime());
    // keep track of which components have finished
    q2_instructionsComponents = [];
    q2_instructionsComponents.push(text_155);
    
    q2_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function q2_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'q2_instructions' ---
    // get current time
    t = q2_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_155* updates
    if (t >= 0.0 && text_155.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_155.tStart = t;  // (not accounting for frame time here)
      text_155.frameNStart = frameN;  // exact frame index
      
      text_155.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_155.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_155.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    q2_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function q2_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'q2_instructions' ---
    q2_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('q2_instructions.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_41_allKeys;
var AM1Components;
function AM1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AM1' ---
    t = 0;
    AM1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('AM1.started', globalClock.getTime());
    key_resp_41.keys = undefined;
    key_resp_41.rt = undefined;
    _key_resp_41_allKeys = [];
    // keep track of which components have finished
    AM1Components = [];
    AM1Components.push(text_156);
    AM1Components.push(text_157);
    AM1Components.push(text_158);
    AM1Components.push(key_resp_41);
    
    AM1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AM1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AM1' ---
    // get current time
    t = AM1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_156* updates
    if (t >= 0.0 && text_156.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_156.tStart = t;  // (not accounting for frame time here)
      text_156.frameNStart = frameN;  // exact frame index
      
      text_156.setAutoDraw(true);
    }
    
    
    // *text_157* updates
    if (t >= 0.0 && text_157.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_157.tStart = t;  // (not accounting for frame time here)
      text_157.frameNStart = frameN;  // exact frame index
      
      text_157.setAutoDraw(true);
    }
    
    
    // *text_158* updates
    if (t >= 0.0 && text_158.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_158.tStart = t;  // (not accounting for frame time here)
      text_158.frameNStart = frameN;  // exact frame index
      
      text_158.setAutoDraw(true);
    }
    
    
    // *key_resp_41* updates
    if (t >= 0.0 && key_resp_41.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_41.tStart = t;  // (not accounting for frame time here)
      key_resp_41.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_41.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_41.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_41.clearEvents(); });
    }
    
    if (key_resp_41.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_41.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_41_allKeys = _key_resp_41_allKeys.concat(theseKeys);
      if (_key_resp_41_allKeys.length > 0) {
        key_resp_41.keys = _key_resp_41_allKeys[_key_resp_41_allKeys.length - 1].name;  // just the last key pressed
        key_resp_41.rt = _key_resp_41_allKeys[_key_resp_41_allKeys.length - 1].rt;
        key_resp_41.duration = _key_resp_41_allKeys[_key_resp_41_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AM1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AM1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AM1' ---
    AM1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AM1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_41.corr, level);
    }
    psychoJS.experiment.addData('key_resp_41.keys', key_resp_41.keys);
    if (typeof key_resp_41.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_41.rt', key_resp_41.rt);
        psychoJS.experiment.addData('key_resp_41.duration', key_resp_41.duration);
        routineTimer.reset();
        }
    
    key_resp_41.stop();
    // the Routine "AM1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_42_allKeys;
var AM2Components;
function AM2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AM2' ---
    t = 0;
    AM2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('AM2.started', globalClock.getTime());
    key_resp_42.keys = undefined;
    key_resp_42.rt = undefined;
    _key_resp_42_allKeys = [];
    // keep track of which components have finished
    AM2Components = [];
    AM2Components.push(text_159);
    AM2Components.push(text_160);
    AM2Components.push(text_161);
    AM2Components.push(key_resp_42);
    
    AM2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AM2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AM2' ---
    // get current time
    t = AM2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_159* updates
    if (t >= 0.0 && text_159.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_159.tStart = t;  // (not accounting for frame time here)
      text_159.frameNStart = frameN;  // exact frame index
      
      text_159.setAutoDraw(true);
    }
    
    
    // *text_160* updates
    if (t >= 0.0 && text_160.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_160.tStart = t;  // (not accounting for frame time here)
      text_160.frameNStart = frameN;  // exact frame index
      
      text_160.setAutoDraw(true);
    }
    
    
    // *text_161* updates
    if (t >= 0.0 && text_161.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_161.tStart = t;  // (not accounting for frame time here)
      text_161.frameNStart = frameN;  // exact frame index
      
      text_161.setAutoDraw(true);
    }
    
    
    // *key_resp_42* updates
    if (t >= 0.0 && key_resp_42.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_42.tStart = t;  // (not accounting for frame time here)
      key_resp_42.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_42.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_42.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_42.clearEvents(); });
    }
    
    if (key_resp_42.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_42.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_42_allKeys = _key_resp_42_allKeys.concat(theseKeys);
      if (_key_resp_42_allKeys.length > 0) {
        key_resp_42.keys = _key_resp_42_allKeys[_key_resp_42_allKeys.length - 1].name;  // just the last key pressed
        key_resp_42.rt = _key_resp_42_allKeys[_key_resp_42_allKeys.length - 1].rt;
        key_resp_42.duration = _key_resp_42_allKeys[_key_resp_42_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AM2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AM2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AM2' ---
    AM2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AM2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_42.corr, level);
    }
    psychoJS.experiment.addData('key_resp_42.keys', key_resp_42.keys);
    if (typeof key_resp_42.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_42.rt', key_resp_42.rt);
        psychoJS.experiment.addData('key_resp_42.duration', key_resp_42.duration);
        routineTimer.reset();
        }
    
    key_resp_42.stop();
    // the Routine "AM2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_43_allKeys;
var AM3Components;
function AM3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AM3' ---
    t = 0;
    AM3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('AM3.started', globalClock.getTime());
    key_resp_43.keys = undefined;
    key_resp_43.rt = undefined;
    _key_resp_43_allKeys = [];
    // keep track of which components have finished
    AM3Components = [];
    AM3Components.push(text_162);
    AM3Components.push(text_163);
    AM3Components.push(text_164);
    AM3Components.push(key_resp_43);
    
    AM3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AM3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AM3' ---
    // get current time
    t = AM3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_162* updates
    if (t >= 0.0 && text_162.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_162.tStart = t;  // (not accounting for frame time here)
      text_162.frameNStart = frameN;  // exact frame index
      
      text_162.setAutoDraw(true);
    }
    
    
    // *text_163* updates
    if (t >= 0.0 && text_163.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_163.tStart = t;  // (not accounting for frame time here)
      text_163.frameNStart = frameN;  // exact frame index
      
      text_163.setAutoDraw(true);
    }
    
    
    // *text_164* updates
    if (t >= 0.0 && text_164.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_164.tStart = t;  // (not accounting for frame time here)
      text_164.frameNStart = frameN;  // exact frame index
      
      text_164.setAutoDraw(true);
    }
    
    
    // *key_resp_43* updates
    if (t >= 0.0 && key_resp_43.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_43.tStart = t;  // (not accounting for frame time here)
      key_resp_43.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_43.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_43.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_43.clearEvents(); });
    }
    
    if (key_resp_43.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_43.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_43_allKeys = _key_resp_43_allKeys.concat(theseKeys);
      if (_key_resp_43_allKeys.length > 0) {
        key_resp_43.keys = _key_resp_43_allKeys[_key_resp_43_allKeys.length - 1].name;  // just the last key pressed
        key_resp_43.rt = _key_resp_43_allKeys[_key_resp_43_allKeys.length - 1].rt;
        key_resp_43.duration = _key_resp_43_allKeys[_key_resp_43_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AM3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AM3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AM3' ---
    AM3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AM3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_43.corr, level);
    }
    psychoJS.experiment.addData('key_resp_43.keys', key_resp_43.keys);
    if (typeof key_resp_43.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_43.rt', key_resp_43.rt);
        psychoJS.experiment.addData('key_resp_43.duration', key_resp_43.duration);
        routineTimer.reset();
        }
    
    key_resp_43.stop();
    // the Routine "AM3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_44_allKeys;
var AM4Components;
function AM4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AM4' ---
    t = 0;
    AM4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('AM4.started', globalClock.getTime());
    key_resp_44.keys = undefined;
    key_resp_44.rt = undefined;
    _key_resp_44_allKeys = [];
    // keep track of which components have finished
    AM4Components = [];
    AM4Components.push(text_165);
    AM4Components.push(text_166);
    AM4Components.push(text_167);
    AM4Components.push(key_resp_44);
    
    AM4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AM4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AM4' ---
    // get current time
    t = AM4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_165* updates
    if (t >= 0.0 && text_165.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_165.tStart = t;  // (not accounting for frame time here)
      text_165.frameNStart = frameN;  // exact frame index
      
      text_165.setAutoDraw(true);
    }
    
    
    // *text_166* updates
    if (t >= 0.0 && text_166.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_166.tStart = t;  // (not accounting for frame time here)
      text_166.frameNStart = frameN;  // exact frame index
      
      text_166.setAutoDraw(true);
    }
    
    
    // *text_167* updates
    if (t >= 0.0 && text_167.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_167.tStart = t;  // (not accounting for frame time here)
      text_167.frameNStart = frameN;  // exact frame index
      
      text_167.setAutoDraw(true);
    }
    
    
    // *key_resp_44* updates
    if (t >= 0.0 && key_resp_44.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_44.tStart = t;  // (not accounting for frame time here)
      key_resp_44.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_44.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_44.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_44.clearEvents(); });
    }
    
    if (key_resp_44.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_44.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_44_allKeys = _key_resp_44_allKeys.concat(theseKeys);
      if (_key_resp_44_allKeys.length > 0) {
        key_resp_44.keys = _key_resp_44_allKeys[_key_resp_44_allKeys.length - 1].name;  // just the last key pressed
        key_resp_44.rt = _key_resp_44_allKeys[_key_resp_44_allKeys.length - 1].rt;
        key_resp_44.duration = _key_resp_44_allKeys[_key_resp_44_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AM4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AM4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AM4' ---
    AM4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AM4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_44.corr, level);
    }
    psychoJS.experiment.addData('key_resp_44.keys', key_resp_44.keys);
    if (typeof key_resp_44.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_44.rt', key_resp_44.rt);
        psychoJS.experiment.addData('key_resp_44.duration', key_resp_44.duration);
        routineTimer.reset();
        }
    
    key_resp_44.stop();
    // the Routine "AM4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_45_allKeys;
var AM5Components;
function AM5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AM5' ---
    t = 0;
    AM5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('AM5.started', globalClock.getTime());
    key_resp_45.keys = undefined;
    key_resp_45.rt = undefined;
    _key_resp_45_allKeys = [];
    // keep track of which components have finished
    AM5Components = [];
    AM5Components.push(text_168);
    AM5Components.push(text_169);
    AM5Components.push(text_170);
    AM5Components.push(key_resp_45);
    
    AM5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function AM5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AM5' ---
    // get current time
    t = AM5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_168* updates
    if (t >= 0.0 && text_168.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_168.tStart = t;  // (not accounting for frame time here)
      text_168.frameNStart = frameN;  // exact frame index
      
      text_168.setAutoDraw(true);
    }
    
    
    // *text_169* updates
    if (t >= 0.0 && text_169.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_169.tStart = t;  // (not accounting for frame time here)
      text_169.frameNStart = frameN;  // exact frame index
      
      text_169.setAutoDraw(true);
    }
    
    
    // *text_170* updates
    if (t >= 0.0 && text_170.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_170.tStart = t;  // (not accounting for frame time here)
      text_170.frameNStart = frameN;  // exact frame index
      
      text_170.setAutoDraw(true);
    }
    
    
    // *key_resp_45* updates
    if (t >= 0.0 && key_resp_45.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_45.tStart = t;  // (not accounting for frame time here)
      key_resp_45.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_45.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_45.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_45.clearEvents(); });
    }
    
    if (key_resp_45.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_45.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_45_allKeys = _key_resp_45_allKeys.concat(theseKeys);
      if (_key_resp_45_allKeys.length > 0) {
        key_resp_45.keys = _key_resp_45_allKeys[_key_resp_45_allKeys.length - 1].name;  // just the last key pressed
        key_resp_45.rt = _key_resp_45_allKeys[_key_resp_45_allKeys.length - 1].rt;
        key_resp_45.duration = _key_resp_45_allKeys[_key_resp_45_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    AM5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AM5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AM5' ---
    AM5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('AM5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_45.corr, level);
    }
    psychoJS.experiment.addData('key_resp_45.keys', key_resp_45.keys);
    if (typeof key_resp_45.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_45.rt', key_resp_45.rt);
        psychoJS.experiment.addData('key_resp_45.duration', key_resp_45.duration);
        routineTimer.reset();
        }
    
    key_resp_45.stop();
    // the Routine "AM5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var q3_instructionsComponents;
function q3_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'q3_instructions' ---
    t = 0;
    q3_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('q3_instructions.started', globalClock.getTime());
    // keep track of which components have finished
    q3_instructionsComponents = [];
    q3_instructionsComponents.push(text_171);
    
    q3_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function q3_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'q3_instructions' ---
    // get current time
    t = q3_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_171* updates
    if (t >= 0.0 && text_171.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_171.tStart = t;  // (not accounting for frame time here)
      text_171.frameNStart = frameN;  // exact frame index
      
      text_171.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_171.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_171.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    q3_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function q3_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'q3_instructions' ---
    q3_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('q3_instructions.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_46_allKeys;
var SPQ1Components;
function SPQ1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ1' ---
    t = 0;
    SPQ1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ1.started', globalClock.getTime());
    key_resp_46.keys = undefined;
    key_resp_46.rt = undefined;
    _key_resp_46_allKeys = [];
    // keep track of which components have finished
    SPQ1Components = [];
    SPQ1Components.push(text_173);
    SPQ1Components.push(text_174);
    SPQ1Components.push(key_resp_46);
    
    SPQ1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ1' ---
    // get current time
    t = SPQ1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_173* updates
    if (t >= 0.0 && text_173.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_173.tStart = t;  // (not accounting for frame time here)
      text_173.frameNStart = frameN;  // exact frame index
      
      text_173.setAutoDraw(true);
    }
    
    
    // *text_174* updates
    if (t >= 0.0 && text_174.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_174.tStart = t;  // (not accounting for frame time here)
      text_174.frameNStart = frameN;  // exact frame index
      
      text_174.setAutoDraw(true);
    }
    
    
    // *key_resp_46* updates
    if (t >= 0.0 && key_resp_46.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_46.tStart = t;  // (not accounting for frame time here)
      key_resp_46.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_46.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_46.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_46.clearEvents(); });
    }
    
    if (key_resp_46.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_46.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_46_allKeys = _key_resp_46_allKeys.concat(theseKeys);
      if (_key_resp_46_allKeys.length > 0) {
        key_resp_46.keys = _key_resp_46_allKeys[_key_resp_46_allKeys.length - 1].name;  // just the last key pressed
        key_resp_46.rt = _key_resp_46_allKeys[_key_resp_46_allKeys.length - 1].rt;
        key_resp_46.duration = _key_resp_46_allKeys[_key_resp_46_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ1' ---
    SPQ1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_46.corr, level);
    }
    psychoJS.experiment.addData('key_resp_46.keys', key_resp_46.keys);
    if (typeof key_resp_46.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_46.rt', key_resp_46.rt);
        psychoJS.experiment.addData('key_resp_46.duration', key_resp_46.duration);
        routineTimer.reset();
        }
    
    key_resp_46.stop();
    // the Routine "SPQ1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_47_allKeys;
var SPQ2Components;
function SPQ2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ2' ---
    t = 0;
    SPQ2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ2.started', globalClock.getTime());
    key_resp_47.keys = undefined;
    key_resp_47.rt = undefined;
    _key_resp_47_allKeys = [];
    // keep track of which components have finished
    SPQ2Components = [];
    SPQ2Components.push(text_175);
    SPQ2Components.push(text_176);
    SPQ2Components.push(key_resp_47);
    
    SPQ2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ2' ---
    // get current time
    t = SPQ2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_175* updates
    if (t >= 0.0 && text_175.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_175.tStart = t;  // (not accounting for frame time here)
      text_175.frameNStart = frameN;  // exact frame index
      
      text_175.setAutoDraw(true);
    }
    
    
    // *text_176* updates
    if (t >= 0.0 && text_176.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_176.tStart = t;  // (not accounting for frame time here)
      text_176.frameNStart = frameN;  // exact frame index
      
      text_176.setAutoDraw(true);
    }
    
    
    // *key_resp_47* updates
    if (t >= 0.0 && key_resp_47.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_47.tStart = t;  // (not accounting for frame time here)
      key_resp_47.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_47.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_47.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_47.clearEvents(); });
    }
    
    if (key_resp_47.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_47.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_47_allKeys = _key_resp_47_allKeys.concat(theseKeys);
      if (_key_resp_47_allKeys.length > 0) {
        key_resp_47.keys = _key_resp_47_allKeys[_key_resp_47_allKeys.length - 1].name;  // just the last key pressed
        key_resp_47.rt = _key_resp_47_allKeys[_key_resp_47_allKeys.length - 1].rt;
        key_resp_47.duration = _key_resp_47_allKeys[_key_resp_47_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ2' ---
    SPQ2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_47.corr, level);
    }
    psychoJS.experiment.addData('key_resp_47.keys', key_resp_47.keys);
    if (typeof key_resp_47.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_47.rt', key_resp_47.rt);
        psychoJS.experiment.addData('key_resp_47.duration', key_resp_47.duration);
        routineTimer.reset();
        }
    
    key_resp_47.stop();
    // the Routine "SPQ2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_48_allKeys;
var SPQ3Components;
function SPQ3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ3' ---
    t = 0;
    SPQ3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ3.started', globalClock.getTime());
    key_resp_48.keys = undefined;
    key_resp_48.rt = undefined;
    _key_resp_48_allKeys = [];
    // keep track of which components have finished
    SPQ3Components = [];
    SPQ3Components.push(text_177);
    SPQ3Components.push(text_178);
    SPQ3Components.push(key_resp_48);
    
    SPQ3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ3' ---
    // get current time
    t = SPQ3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_177* updates
    if (t >= 0.0 && text_177.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_177.tStart = t;  // (not accounting for frame time here)
      text_177.frameNStart = frameN;  // exact frame index
      
      text_177.setAutoDraw(true);
    }
    
    
    // *text_178* updates
    if (t >= 0.0 && text_178.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_178.tStart = t;  // (not accounting for frame time here)
      text_178.frameNStart = frameN;  // exact frame index
      
      text_178.setAutoDraw(true);
    }
    
    
    // *key_resp_48* updates
    if (t >= 0.0 && key_resp_48.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_48.tStart = t;  // (not accounting for frame time here)
      key_resp_48.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_48.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_48.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_48.clearEvents(); });
    }
    
    if (key_resp_48.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_48.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_48_allKeys = _key_resp_48_allKeys.concat(theseKeys);
      if (_key_resp_48_allKeys.length > 0) {
        key_resp_48.keys = _key_resp_48_allKeys[_key_resp_48_allKeys.length - 1].name;  // just the last key pressed
        key_resp_48.rt = _key_resp_48_allKeys[_key_resp_48_allKeys.length - 1].rt;
        key_resp_48.duration = _key_resp_48_allKeys[_key_resp_48_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ3' ---
    SPQ3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_48.corr, level);
    }
    psychoJS.experiment.addData('key_resp_48.keys', key_resp_48.keys);
    if (typeof key_resp_48.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_48.rt', key_resp_48.rt);
        psychoJS.experiment.addData('key_resp_48.duration', key_resp_48.duration);
        routineTimer.reset();
        }
    
    key_resp_48.stop();
    // the Routine "SPQ3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_49_allKeys;
var SPQ4Components;
function SPQ4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ4' ---
    t = 0;
    SPQ4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ4.started', globalClock.getTime());
    key_resp_49.keys = undefined;
    key_resp_49.rt = undefined;
    _key_resp_49_allKeys = [];
    // keep track of which components have finished
    SPQ4Components = [];
    SPQ4Components.push(text_179);
    SPQ4Components.push(text_180);
    SPQ4Components.push(key_resp_49);
    
    SPQ4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ4' ---
    // get current time
    t = SPQ4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_179* updates
    if (t >= 0.0 && text_179.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_179.tStart = t;  // (not accounting for frame time here)
      text_179.frameNStart = frameN;  // exact frame index
      
      text_179.setAutoDraw(true);
    }
    
    
    // *text_180* updates
    if (t >= 0.0 && text_180.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_180.tStart = t;  // (not accounting for frame time here)
      text_180.frameNStart = frameN;  // exact frame index
      
      text_180.setAutoDraw(true);
    }
    
    
    // *key_resp_49* updates
    if (t >= 0.0 && key_resp_49.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_49.tStart = t;  // (not accounting for frame time here)
      key_resp_49.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_49.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_49.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_49.clearEvents(); });
    }
    
    if (key_resp_49.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_49.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_49_allKeys = _key_resp_49_allKeys.concat(theseKeys);
      if (_key_resp_49_allKeys.length > 0) {
        key_resp_49.keys = _key_resp_49_allKeys[_key_resp_49_allKeys.length - 1].name;  // just the last key pressed
        key_resp_49.rt = _key_resp_49_allKeys[_key_resp_49_allKeys.length - 1].rt;
        key_resp_49.duration = _key_resp_49_allKeys[_key_resp_49_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ4' ---
    SPQ4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_49.corr, level);
    }
    psychoJS.experiment.addData('key_resp_49.keys', key_resp_49.keys);
    if (typeof key_resp_49.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_49.rt', key_resp_49.rt);
        psychoJS.experiment.addData('key_resp_49.duration', key_resp_49.duration);
        routineTimer.reset();
        }
    
    key_resp_49.stop();
    // the Routine "SPQ4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_50_allKeys;
var SPQ5Components;
function SPQ5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ5' ---
    t = 0;
    SPQ5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ5.started', globalClock.getTime());
    key_resp_50.keys = undefined;
    key_resp_50.rt = undefined;
    _key_resp_50_allKeys = [];
    // keep track of which components have finished
    SPQ5Components = [];
    SPQ5Components.push(text_181);
    SPQ5Components.push(text_182);
    SPQ5Components.push(key_resp_50);
    
    SPQ5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ5' ---
    // get current time
    t = SPQ5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_181* updates
    if (t >= 0.0 && text_181.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_181.tStart = t;  // (not accounting for frame time here)
      text_181.frameNStart = frameN;  // exact frame index
      
      text_181.setAutoDraw(true);
    }
    
    
    // *text_182* updates
    if (t >= 0.0 && text_182.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_182.tStart = t;  // (not accounting for frame time here)
      text_182.frameNStart = frameN;  // exact frame index
      
      text_182.setAutoDraw(true);
    }
    
    
    // *key_resp_50* updates
    if (t >= 0.0 && key_resp_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_50.tStart = t;  // (not accounting for frame time here)
      key_resp_50.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_50.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_50.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_50.clearEvents(); });
    }
    
    if (key_resp_50.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_50.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_50_allKeys = _key_resp_50_allKeys.concat(theseKeys);
      if (_key_resp_50_allKeys.length > 0) {
        key_resp_50.keys = _key_resp_50_allKeys[_key_resp_50_allKeys.length - 1].name;  // just the last key pressed
        key_resp_50.rt = _key_resp_50_allKeys[_key_resp_50_allKeys.length - 1].rt;
        key_resp_50.duration = _key_resp_50_allKeys[_key_resp_50_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ5' ---
    SPQ5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_50.corr, level);
    }
    psychoJS.experiment.addData('key_resp_50.keys', key_resp_50.keys);
    if (typeof key_resp_50.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_50.rt', key_resp_50.rt);
        psychoJS.experiment.addData('key_resp_50.duration', key_resp_50.duration);
        routineTimer.reset();
        }
    
    key_resp_50.stop();
    // the Routine "SPQ5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_51_allKeys;
var SPQ6Components;
function SPQ6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ6' ---
    t = 0;
    SPQ6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ6.started', globalClock.getTime());
    key_resp_51.keys = undefined;
    key_resp_51.rt = undefined;
    _key_resp_51_allKeys = [];
    // keep track of which components have finished
    SPQ6Components = [];
    SPQ6Components.push(text_183);
    SPQ6Components.push(text_184);
    SPQ6Components.push(key_resp_51);
    
    SPQ6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ6' ---
    // get current time
    t = SPQ6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_183* updates
    if (t >= 0.0 && text_183.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_183.tStart = t;  // (not accounting for frame time here)
      text_183.frameNStart = frameN;  // exact frame index
      
      text_183.setAutoDraw(true);
    }
    
    
    // *text_184* updates
    if (t >= 0.0 && text_184.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_184.tStart = t;  // (not accounting for frame time here)
      text_184.frameNStart = frameN;  // exact frame index
      
      text_184.setAutoDraw(true);
    }
    
    
    // *key_resp_51* updates
    if (t >= 0.0 && key_resp_51.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_51.tStart = t;  // (not accounting for frame time here)
      key_resp_51.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_51.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_51.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_51.clearEvents(); });
    }
    
    if (key_resp_51.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_51.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_51_allKeys = _key_resp_51_allKeys.concat(theseKeys);
      if (_key_resp_51_allKeys.length > 0) {
        key_resp_51.keys = _key_resp_51_allKeys[_key_resp_51_allKeys.length - 1].name;  // just the last key pressed
        key_resp_51.rt = _key_resp_51_allKeys[_key_resp_51_allKeys.length - 1].rt;
        key_resp_51.duration = _key_resp_51_allKeys[_key_resp_51_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ6' ---
    SPQ6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ6.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_51.corr, level);
    }
    psychoJS.experiment.addData('key_resp_51.keys', key_resp_51.keys);
    if (typeof key_resp_51.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_51.rt', key_resp_51.rt);
        psychoJS.experiment.addData('key_resp_51.duration', key_resp_51.duration);
        routineTimer.reset();
        }
    
    key_resp_51.stop();
    // the Routine "SPQ6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_52_allKeys;
var SPQ7Components;
function SPQ7RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ7' ---
    t = 0;
    SPQ7Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ7.started', globalClock.getTime());
    key_resp_52.keys = undefined;
    key_resp_52.rt = undefined;
    _key_resp_52_allKeys = [];
    // keep track of which components have finished
    SPQ7Components = [];
    SPQ7Components.push(text_185);
    SPQ7Components.push(text_186);
    SPQ7Components.push(key_resp_52);
    
    SPQ7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ7RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ7' ---
    // get current time
    t = SPQ7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_185* updates
    if (t >= 0.0 && text_185.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_185.tStart = t;  // (not accounting for frame time here)
      text_185.frameNStart = frameN;  // exact frame index
      
      text_185.setAutoDraw(true);
    }
    
    
    // *text_186* updates
    if (t >= 0.0 && text_186.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_186.tStart = t;  // (not accounting for frame time here)
      text_186.frameNStart = frameN;  // exact frame index
      
      text_186.setAutoDraw(true);
    }
    
    
    // *key_resp_52* updates
    if (t >= 0.0 && key_resp_52.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_52.tStart = t;  // (not accounting for frame time here)
      key_resp_52.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_52.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_52.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_52.clearEvents(); });
    }
    
    if (key_resp_52.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_52.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_52_allKeys = _key_resp_52_allKeys.concat(theseKeys);
      if (_key_resp_52_allKeys.length > 0) {
        key_resp_52.keys = _key_resp_52_allKeys[_key_resp_52_allKeys.length - 1].name;  // just the last key pressed
        key_resp_52.rt = _key_resp_52_allKeys[_key_resp_52_allKeys.length - 1].rt;
        key_resp_52.duration = _key_resp_52_allKeys[_key_resp_52_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ7RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ7' ---
    SPQ7Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ7.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_52.corr, level);
    }
    psychoJS.experiment.addData('key_resp_52.keys', key_resp_52.keys);
    if (typeof key_resp_52.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_52.rt', key_resp_52.rt);
        psychoJS.experiment.addData('key_resp_52.duration', key_resp_52.duration);
        routineTimer.reset();
        }
    
    key_resp_52.stop();
    // the Routine "SPQ7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_53_allKeys;
var SPQ8Components;
function SPQ8RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ8' ---
    t = 0;
    SPQ8Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ8.started', globalClock.getTime());
    key_resp_53.keys = undefined;
    key_resp_53.rt = undefined;
    _key_resp_53_allKeys = [];
    // keep track of which components have finished
    SPQ8Components = [];
    SPQ8Components.push(text_187);
    SPQ8Components.push(text_188);
    SPQ8Components.push(key_resp_53);
    
    SPQ8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ8RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ8' ---
    // get current time
    t = SPQ8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_187* updates
    if (t >= 0.0 && text_187.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_187.tStart = t;  // (not accounting for frame time here)
      text_187.frameNStart = frameN;  // exact frame index
      
      text_187.setAutoDraw(true);
    }
    
    
    // *text_188* updates
    if (t >= 0.0 && text_188.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_188.tStart = t;  // (not accounting for frame time here)
      text_188.frameNStart = frameN;  // exact frame index
      
      text_188.setAutoDraw(true);
    }
    
    
    // *key_resp_53* updates
    if (t >= 0.0 && key_resp_53.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_53.tStart = t;  // (not accounting for frame time here)
      key_resp_53.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_53.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_53.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_53.clearEvents(); });
    }
    
    if (key_resp_53.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_53.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_53_allKeys = _key_resp_53_allKeys.concat(theseKeys);
      if (_key_resp_53_allKeys.length > 0) {
        key_resp_53.keys = _key_resp_53_allKeys[_key_resp_53_allKeys.length - 1].name;  // just the last key pressed
        key_resp_53.rt = _key_resp_53_allKeys[_key_resp_53_allKeys.length - 1].rt;
        key_resp_53.duration = _key_resp_53_allKeys[_key_resp_53_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ8RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ8' ---
    SPQ8Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ8.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_53.corr, level);
    }
    psychoJS.experiment.addData('key_resp_53.keys', key_resp_53.keys);
    if (typeof key_resp_53.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_53.rt', key_resp_53.rt);
        psychoJS.experiment.addData('key_resp_53.duration', key_resp_53.duration);
        routineTimer.reset();
        }
    
    key_resp_53.stop();
    // the Routine "SPQ8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_54_allKeys;
var SPQ9Components;
function SPQ9RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ9' ---
    t = 0;
    SPQ9Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ9.started', globalClock.getTime());
    key_resp_54.keys = undefined;
    key_resp_54.rt = undefined;
    _key_resp_54_allKeys = [];
    // keep track of which components have finished
    SPQ9Components = [];
    SPQ9Components.push(text_189);
    SPQ9Components.push(text_190);
    SPQ9Components.push(key_resp_54);
    
    SPQ9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ9RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ9' ---
    // get current time
    t = SPQ9Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_189* updates
    if (t >= 0.0 && text_189.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_189.tStart = t;  // (not accounting for frame time here)
      text_189.frameNStart = frameN;  // exact frame index
      
      text_189.setAutoDraw(true);
    }
    
    
    // *text_190* updates
    if (t >= 0.0 && text_190.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_190.tStart = t;  // (not accounting for frame time here)
      text_190.frameNStart = frameN;  // exact frame index
      
      text_190.setAutoDraw(true);
    }
    
    
    // *key_resp_54* updates
    if (t >= 0.0 && key_resp_54.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_54.tStart = t;  // (not accounting for frame time here)
      key_resp_54.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_54.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_54.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_54.clearEvents(); });
    }
    
    if (key_resp_54.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_54.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_54_allKeys = _key_resp_54_allKeys.concat(theseKeys);
      if (_key_resp_54_allKeys.length > 0) {
        key_resp_54.keys = _key_resp_54_allKeys[_key_resp_54_allKeys.length - 1].name;  // just the last key pressed
        key_resp_54.rt = _key_resp_54_allKeys[_key_resp_54_allKeys.length - 1].rt;
        key_resp_54.duration = _key_resp_54_allKeys[_key_resp_54_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ9RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ9' ---
    SPQ9Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ9.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_54.corr, level);
    }
    psychoJS.experiment.addData('key_resp_54.keys', key_resp_54.keys);
    if (typeof key_resp_54.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_54.rt', key_resp_54.rt);
        psychoJS.experiment.addData('key_resp_54.duration', key_resp_54.duration);
        routineTimer.reset();
        }
    
    key_resp_54.stop();
    // the Routine "SPQ9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_55_allKeys;
var SPQ10Components;
function SPQ10RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ10' ---
    t = 0;
    SPQ10Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ10.started', globalClock.getTime());
    key_resp_55.keys = undefined;
    key_resp_55.rt = undefined;
    _key_resp_55_allKeys = [];
    // keep track of which components have finished
    SPQ10Components = [];
    SPQ10Components.push(text_191);
    SPQ10Components.push(text_192);
    SPQ10Components.push(key_resp_55);
    
    SPQ10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ10RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ10' ---
    // get current time
    t = SPQ10Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_191* updates
    if (t >= 0.0 && text_191.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_191.tStart = t;  // (not accounting for frame time here)
      text_191.frameNStart = frameN;  // exact frame index
      
      text_191.setAutoDraw(true);
    }
    
    
    // *text_192* updates
    if (t >= 0.0 && text_192.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_192.tStart = t;  // (not accounting for frame time here)
      text_192.frameNStart = frameN;  // exact frame index
      
      text_192.setAutoDraw(true);
    }
    
    
    // *key_resp_55* updates
    if (t >= 0.0 && key_resp_55.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_55.tStart = t;  // (not accounting for frame time here)
      key_resp_55.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_55.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_55.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_55.clearEvents(); });
    }
    
    if (key_resp_55.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_55.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_55_allKeys = _key_resp_55_allKeys.concat(theseKeys);
      if (_key_resp_55_allKeys.length > 0) {
        key_resp_55.keys = _key_resp_55_allKeys[_key_resp_55_allKeys.length - 1].name;  // just the last key pressed
        key_resp_55.rt = _key_resp_55_allKeys[_key_resp_55_allKeys.length - 1].rt;
        key_resp_55.duration = _key_resp_55_allKeys[_key_resp_55_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ10RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ10' ---
    SPQ10Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ10.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_55.corr, level);
    }
    psychoJS.experiment.addData('key_resp_55.keys', key_resp_55.keys);
    if (typeof key_resp_55.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_55.rt', key_resp_55.rt);
        psychoJS.experiment.addData('key_resp_55.duration', key_resp_55.duration);
        routineTimer.reset();
        }
    
    key_resp_55.stop();
    // the Routine "SPQ10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_56_allKeys;
var SQP11Components;
function SQP11RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SQP11' ---
    t = 0;
    SQP11Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SQP11.started', globalClock.getTime());
    key_resp_56.keys = undefined;
    key_resp_56.rt = undefined;
    _key_resp_56_allKeys = [];
    // keep track of which components have finished
    SQP11Components = [];
    SQP11Components.push(text_193);
    SQP11Components.push(text_194);
    SQP11Components.push(key_resp_56);
    
    SQP11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SQP11RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SQP11' ---
    // get current time
    t = SQP11Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_193* updates
    if (t >= 0.0 && text_193.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_193.tStart = t;  // (not accounting for frame time here)
      text_193.frameNStart = frameN;  // exact frame index
      
      text_193.setAutoDraw(true);
    }
    
    
    // *text_194* updates
    if (t >= 0.0 && text_194.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_194.tStart = t;  // (not accounting for frame time here)
      text_194.frameNStart = frameN;  // exact frame index
      
      text_194.setAutoDraw(true);
    }
    
    
    // *key_resp_56* updates
    if (t >= 0.0 && key_resp_56.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_56.tStart = t;  // (not accounting for frame time here)
      key_resp_56.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_56.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_56.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_56.clearEvents(); });
    }
    
    if (key_resp_56.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_56.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_56_allKeys = _key_resp_56_allKeys.concat(theseKeys);
      if (_key_resp_56_allKeys.length > 0) {
        key_resp_56.keys = _key_resp_56_allKeys[_key_resp_56_allKeys.length - 1].name;  // just the last key pressed
        key_resp_56.rt = _key_resp_56_allKeys[_key_resp_56_allKeys.length - 1].rt;
        key_resp_56.duration = _key_resp_56_allKeys[_key_resp_56_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SQP11Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SQP11RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SQP11' ---
    SQP11Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SQP11.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_56.corr, level);
    }
    psychoJS.experiment.addData('key_resp_56.keys', key_resp_56.keys);
    if (typeof key_resp_56.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_56.rt', key_resp_56.rt);
        psychoJS.experiment.addData('key_resp_56.duration', key_resp_56.duration);
        routineTimer.reset();
        }
    
    key_resp_56.stop();
    // the Routine "SQP11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_57_allKeys;
var SPQ12Components;
function SPQ12RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ12' ---
    t = 0;
    SPQ12Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ12.started', globalClock.getTime());
    key_resp_57.keys = undefined;
    key_resp_57.rt = undefined;
    _key_resp_57_allKeys = [];
    // keep track of which components have finished
    SPQ12Components = [];
    SPQ12Components.push(text_195);
    SPQ12Components.push(text_196);
    SPQ12Components.push(key_resp_57);
    
    SPQ12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ12RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ12' ---
    // get current time
    t = SPQ12Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_195* updates
    if (t >= 0.0 && text_195.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_195.tStart = t;  // (not accounting for frame time here)
      text_195.frameNStart = frameN;  // exact frame index
      
      text_195.setAutoDraw(true);
    }
    
    
    // *text_196* updates
    if (t >= 0.0 && text_196.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_196.tStart = t;  // (not accounting for frame time here)
      text_196.frameNStart = frameN;  // exact frame index
      
      text_196.setAutoDraw(true);
    }
    
    
    // *key_resp_57* updates
    if (t >= 0.0 && key_resp_57.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_57.tStart = t;  // (not accounting for frame time here)
      key_resp_57.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_57.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_57.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_57.clearEvents(); });
    }
    
    if (key_resp_57.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_57.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_57_allKeys = _key_resp_57_allKeys.concat(theseKeys);
      if (_key_resp_57_allKeys.length > 0) {
        key_resp_57.keys = _key_resp_57_allKeys[_key_resp_57_allKeys.length - 1].name;  // just the last key pressed
        key_resp_57.rt = _key_resp_57_allKeys[_key_resp_57_allKeys.length - 1].rt;
        key_resp_57.duration = _key_resp_57_allKeys[_key_resp_57_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ12Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ12RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ12' ---
    SPQ12Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ12.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_57.corr, level);
    }
    psychoJS.experiment.addData('key_resp_57.keys', key_resp_57.keys);
    if (typeof key_resp_57.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_57.rt', key_resp_57.rt);
        psychoJS.experiment.addData('key_resp_57.duration', key_resp_57.duration);
        routineTimer.reset();
        }
    
    key_resp_57.stop();
    // the Routine "SPQ12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_58_allKeys;
var SPQ13Components;
function SPQ13RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ13' ---
    t = 0;
    SPQ13Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ13.started', globalClock.getTime());
    key_resp_58.keys = undefined;
    key_resp_58.rt = undefined;
    _key_resp_58_allKeys = [];
    // keep track of which components have finished
    SPQ13Components = [];
    SPQ13Components.push(text_197);
    SPQ13Components.push(text_198);
    SPQ13Components.push(key_resp_58);
    
    SPQ13Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ13RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ13' ---
    // get current time
    t = SPQ13Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_197* updates
    if (t >= 0.0 && text_197.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_197.tStart = t;  // (not accounting for frame time here)
      text_197.frameNStart = frameN;  // exact frame index
      
      text_197.setAutoDraw(true);
    }
    
    
    // *text_198* updates
    if (t >= 0.0 && text_198.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_198.tStart = t;  // (not accounting for frame time here)
      text_198.frameNStart = frameN;  // exact frame index
      
      text_198.setAutoDraw(true);
    }
    
    
    // *key_resp_58* updates
    if (t >= 0.0 && key_resp_58.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_58.tStart = t;  // (not accounting for frame time here)
      key_resp_58.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_58.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_58.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_58.clearEvents(); });
    }
    
    if (key_resp_58.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_58.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_58_allKeys = _key_resp_58_allKeys.concat(theseKeys);
      if (_key_resp_58_allKeys.length > 0) {
        key_resp_58.keys = _key_resp_58_allKeys[_key_resp_58_allKeys.length - 1].name;  // just the last key pressed
        key_resp_58.rt = _key_resp_58_allKeys[_key_resp_58_allKeys.length - 1].rt;
        key_resp_58.duration = _key_resp_58_allKeys[_key_resp_58_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ13Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ13RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ13' ---
    SPQ13Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ13.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_58.corr, level);
    }
    psychoJS.experiment.addData('key_resp_58.keys', key_resp_58.keys);
    if (typeof key_resp_58.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_58.rt', key_resp_58.rt);
        psychoJS.experiment.addData('key_resp_58.duration', key_resp_58.duration);
        routineTimer.reset();
        }
    
    key_resp_58.stop();
    // the Routine "SPQ13" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_59_allKeys;
var SPQ14Components;
function SPQ14RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ14' ---
    t = 0;
    SPQ14Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ14.started', globalClock.getTime());
    key_resp_59.keys = undefined;
    key_resp_59.rt = undefined;
    _key_resp_59_allKeys = [];
    // keep track of which components have finished
    SPQ14Components = [];
    SPQ14Components.push(text_199);
    SPQ14Components.push(text_200);
    SPQ14Components.push(key_resp_59);
    
    SPQ14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ14RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ14' ---
    // get current time
    t = SPQ14Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_199* updates
    if (t >= 0.0 && text_199.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_199.tStart = t;  // (not accounting for frame time here)
      text_199.frameNStart = frameN;  // exact frame index
      
      text_199.setAutoDraw(true);
    }
    
    
    // *text_200* updates
    if (t >= 0.0 && text_200.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_200.tStart = t;  // (not accounting for frame time here)
      text_200.frameNStart = frameN;  // exact frame index
      
      text_200.setAutoDraw(true);
    }
    
    
    // *key_resp_59* updates
    if (t >= 0.0 && key_resp_59.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_59.tStart = t;  // (not accounting for frame time here)
      key_resp_59.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_59.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_59.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_59.clearEvents(); });
    }
    
    if (key_resp_59.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_59.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_59_allKeys = _key_resp_59_allKeys.concat(theseKeys);
      if (_key_resp_59_allKeys.length > 0) {
        key_resp_59.keys = _key_resp_59_allKeys[_key_resp_59_allKeys.length - 1].name;  // just the last key pressed
        key_resp_59.rt = _key_resp_59_allKeys[_key_resp_59_allKeys.length - 1].rt;
        key_resp_59.duration = _key_resp_59_allKeys[_key_resp_59_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ14Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ14RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ14' ---
    SPQ14Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ14.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_59.corr, level);
    }
    psychoJS.experiment.addData('key_resp_59.keys', key_resp_59.keys);
    if (typeof key_resp_59.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_59.rt', key_resp_59.rt);
        psychoJS.experiment.addData('key_resp_59.duration', key_resp_59.duration);
        routineTimer.reset();
        }
    
    key_resp_59.stop();
    // the Routine "SPQ14" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_60_allKeys;
var SPQ15Components;
function SPQ15RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ15' ---
    t = 0;
    SPQ15Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ15.started', globalClock.getTime());
    key_resp_60.keys = undefined;
    key_resp_60.rt = undefined;
    _key_resp_60_allKeys = [];
    // keep track of which components have finished
    SPQ15Components = [];
    SPQ15Components.push(text_201);
    SPQ15Components.push(text_202);
    SPQ15Components.push(key_resp_60);
    
    SPQ15Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ15RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ15' ---
    // get current time
    t = SPQ15Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_201* updates
    if (t >= 0.0 && text_201.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_201.tStart = t;  // (not accounting for frame time here)
      text_201.frameNStart = frameN;  // exact frame index
      
      text_201.setAutoDraw(true);
    }
    
    
    // *text_202* updates
    if (t >= 0.0 && text_202.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_202.tStart = t;  // (not accounting for frame time here)
      text_202.frameNStart = frameN;  // exact frame index
      
      text_202.setAutoDraw(true);
    }
    
    
    // *key_resp_60* updates
    if (t >= 0.0 && key_resp_60.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_60.tStart = t;  // (not accounting for frame time here)
      key_resp_60.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_60.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_60.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_60.clearEvents(); });
    }
    
    if (key_resp_60.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_60.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_60_allKeys = _key_resp_60_allKeys.concat(theseKeys);
      if (_key_resp_60_allKeys.length > 0) {
        key_resp_60.keys = _key_resp_60_allKeys[_key_resp_60_allKeys.length - 1].name;  // just the last key pressed
        key_resp_60.rt = _key_resp_60_allKeys[_key_resp_60_allKeys.length - 1].rt;
        key_resp_60.duration = _key_resp_60_allKeys[_key_resp_60_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ15Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ15RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ15' ---
    SPQ15Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ15.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_60.corr, level);
    }
    psychoJS.experiment.addData('key_resp_60.keys', key_resp_60.keys);
    if (typeof key_resp_60.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_60.rt', key_resp_60.rt);
        psychoJS.experiment.addData('key_resp_60.duration', key_resp_60.duration);
        routineTimer.reset();
        }
    
    key_resp_60.stop();
    // the Routine "SPQ15" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_61_allKeys;
var SPQ16Components;
function SPQ16RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ16' ---
    t = 0;
    SPQ16Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ16.started', globalClock.getTime());
    key_resp_61.keys = undefined;
    key_resp_61.rt = undefined;
    _key_resp_61_allKeys = [];
    // keep track of which components have finished
    SPQ16Components = [];
    SPQ16Components.push(text_203);
    SPQ16Components.push(text_204);
    SPQ16Components.push(key_resp_61);
    
    SPQ16Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ16RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ16' ---
    // get current time
    t = SPQ16Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_203* updates
    if (t >= 0.0 && text_203.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_203.tStart = t;  // (not accounting for frame time here)
      text_203.frameNStart = frameN;  // exact frame index
      
      text_203.setAutoDraw(true);
    }
    
    
    // *text_204* updates
    if (t >= 0.0 && text_204.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_204.tStart = t;  // (not accounting for frame time here)
      text_204.frameNStart = frameN;  // exact frame index
      
      text_204.setAutoDraw(true);
    }
    
    
    // *key_resp_61* updates
    if (t >= 0.0 && key_resp_61.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_61.tStart = t;  // (not accounting for frame time here)
      key_resp_61.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_61.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_61.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_61.clearEvents(); });
    }
    
    if (key_resp_61.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_61.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_61_allKeys = _key_resp_61_allKeys.concat(theseKeys);
      if (_key_resp_61_allKeys.length > 0) {
        key_resp_61.keys = _key_resp_61_allKeys[_key_resp_61_allKeys.length - 1].name;  // just the last key pressed
        key_resp_61.rt = _key_resp_61_allKeys[_key_resp_61_allKeys.length - 1].rt;
        key_resp_61.duration = _key_resp_61_allKeys[_key_resp_61_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ16Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ16RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ16' ---
    SPQ16Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ16.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_61.corr, level);
    }
    psychoJS.experiment.addData('key_resp_61.keys', key_resp_61.keys);
    if (typeof key_resp_61.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_61.rt', key_resp_61.rt);
        psychoJS.experiment.addData('key_resp_61.duration', key_resp_61.duration);
        routineTimer.reset();
        }
    
    key_resp_61.stop();
    // the Routine "SPQ16" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_62_allKeys;
var SPQ17Components;
function SPQ17RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ17' ---
    t = 0;
    SPQ17Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ17.started', globalClock.getTime());
    key_resp_62.keys = undefined;
    key_resp_62.rt = undefined;
    _key_resp_62_allKeys = [];
    // keep track of which components have finished
    SPQ17Components = [];
    SPQ17Components.push(text_205);
    SPQ17Components.push(text_206);
    SPQ17Components.push(key_resp_62);
    
    SPQ17Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ17RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ17' ---
    // get current time
    t = SPQ17Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_205* updates
    if (t >= 0.0 && text_205.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_205.tStart = t;  // (not accounting for frame time here)
      text_205.frameNStart = frameN;  // exact frame index
      
      text_205.setAutoDraw(true);
    }
    
    
    // *text_206* updates
    if (t >= 0.0 && text_206.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_206.tStart = t;  // (not accounting for frame time here)
      text_206.frameNStart = frameN;  // exact frame index
      
      text_206.setAutoDraw(true);
    }
    
    
    // *key_resp_62* updates
    if (t >= 0.0 && key_resp_62.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_62.tStart = t;  // (not accounting for frame time here)
      key_resp_62.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_62.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_62.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_62.clearEvents(); });
    }
    
    if (key_resp_62.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_62.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_62_allKeys = _key_resp_62_allKeys.concat(theseKeys);
      if (_key_resp_62_allKeys.length > 0) {
        key_resp_62.keys = _key_resp_62_allKeys[_key_resp_62_allKeys.length - 1].name;  // just the last key pressed
        key_resp_62.rt = _key_resp_62_allKeys[_key_resp_62_allKeys.length - 1].rt;
        key_resp_62.duration = _key_resp_62_allKeys[_key_resp_62_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ17Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ17RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ17' ---
    SPQ17Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ17.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_62.corr, level);
    }
    psychoJS.experiment.addData('key_resp_62.keys', key_resp_62.keys);
    if (typeof key_resp_62.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_62.rt', key_resp_62.rt);
        psychoJS.experiment.addData('key_resp_62.duration', key_resp_62.duration);
        routineTimer.reset();
        }
    
    key_resp_62.stop();
    // the Routine "SPQ17" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_63_allKeys;
var SPQ18Components;
function SPQ18RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ18' ---
    t = 0;
    SPQ18Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ18.started', globalClock.getTime());
    key_resp_63.keys = undefined;
    key_resp_63.rt = undefined;
    _key_resp_63_allKeys = [];
    // keep track of which components have finished
    SPQ18Components = [];
    SPQ18Components.push(text_207);
    SPQ18Components.push(text_208);
    SPQ18Components.push(key_resp_63);
    
    SPQ18Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ18RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ18' ---
    // get current time
    t = SPQ18Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_207* updates
    if (t >= 0.0 && text_207.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_207.tStart = t;  // (not accounting for frame time here)
      text_207.frameNStart = frameN;  // exact frame index
      
      text_207.setAutoDraw(true);
    }
    
    
    // *text_208* updates
    if (t >= 0.0 && text_208.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_208.tStart = t;  // (not accounting for frame time here)
      text_208.frameNStart = frameN;  // exact frame index
      
      text_208.setAutoDraw(true);
    }
    
    
    // *key_resp_63* updates
    if (t >= 0.0 && key_resp_63.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_63.tStart = t;  // (not accounting for frame time here)
      key_resp_63.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_63.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_63.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_63.clearEvents(); });
    }
    
    if (key_resp_63.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_63.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_63_allKeys = _key_resp_63_allKeys.concat(theseKeys);
      if (_key_resp_63_allKeys.length > 0) {
        key_resp_63.keys = _key_resp_63_allKeys[_key_resp_63_allKeys.length - 1].name;  // just the last key pressed
        key_resp_63.rt = _key_resp_63_allKeys[_key_resp_63_allKeys.length - 1].rt;
        key_resp_63.duration = _key_resp_63_allKeys[_key_resp_63_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ18Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ18RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ18' ---
    SPQ18Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ18.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_63.corr, level);
    }
    psychoJS.experiment.addData('key_resp_63.keys', key_resp_63.keys);
    if (typeof key_resp_63.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_63.rt', key_resp_63.rt);
        psychoJS.experiment.addData('key_resp_63.duration', key_resp_63.duration);
        routineTimer.reset();
        }
    
    key_resp_63.stop();
    // the Routine "SPQ18" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_64_allKeys;
var SPQ19Components;
function SPQ19RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ19' ---
    t = 0;
    SPQ19Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ19.started', globalClock.getTime());
    key_resp_64.keys = undefined;
    key_resp_64.rt = undefined;
    _key_resp_64_allKeys = [];
    // keep track of which components have finished
    SPQ19Components = [];
    SPQ19Components.push(text_209);
    SPQ19Components.push(text_210);
    SPQ19Components.push(key_resp_64);
    
    SPQ19Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ19RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ19' ---
    // get current time
    t = SPQ19Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_209* updates
    if (t >= 0.0 && text_209.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_209.tStart = t;  // (not accounting for frame time here)
      text_209.frameNStart = frameN;  // exact frame index
      
      text_209.setAutoDraw(true);
    }
    
    
    // *text_210* updates
    if (t >= 0.0 && text_210.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_210.tStart = t;  // (not accounting for frame time here)
      text_210.frameNStart = frameN;  // exact frame index
      
      text_210.setAutoDraw(true);
    }
    
    
    // *key_resp_64* updates
    if (t >= 0.0 && key_resp_64.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_64.tStart = t;  // (not accounting for frame time here)
      key_resp_64.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_64.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_64.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_64.clearEvents(); });
    }
    
    if (key_resp_64.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_64.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_64_allKeys = _key_resp_64_allKeys.concat(theseKeys);
      if (_key_resp_64_allKeys.length > 0) {
        key_resp_64.keys = _key_resp_64_allKeys[_key_resp_64_allKeys.length - 1].name;  // just the last key pressed
        key_resp_64.rt = _key_resp_64_allKeys[_key_resp_64_allKeys.length - 1].rt;
        key_resp_64.duration = _key_resp_64_allKeys[_key_resp_64_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ19Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ19RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ19' ---
    SPQ19Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ19.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_64.corr, level);
    }
    psychoJS.experiment.addData('key_resp_64.keys', key_resp_64.keys);
    if (typeof key_resp_64.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_64.rt', key_resp_64.rt);
        psychoJS.experiment.addData('key_resp_64.duration', key_resp_64.duration);
        routineTimer.reset();
        }
    
    key_resp_64.stop();
    // the Routine "SPQ19" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_65_allKeys;
var SPQ20Components;
function SPQ20RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ20' ---
    t = 0;
    SPQ20Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ20.started', globalClock.getTime());
    key_resp_65.keys = undefined;
    key_resp_65.rt = undefined;
    _key_resp_65_allKeys = [];
    // keep track of which components have finished
    SPQ20Components = [];
    SPQ20Components.push(text_211);
    SPQ20Components.push(text_212);
    SPQ20Components.push(key_resp_65);
    
    SPQ20Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ20RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ20' ---
    // get current time
    t = SPQ20Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_211* updates
    if (t >= 0.0 && text_211.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_211.tStart = t;  // (not accounting for frame time here)
      text_211.frameNStart = frameN;  // exact frame index
      
      text_211.setAutoDraw(true);
    }
    
    
    // *text_212* updates
    if (t >= 0.0 && text_212.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_212.tStart = t;  // (not accounting for frame time here)
      text_212.frameNStart = frameN;  // exact frame index
      
      text_212.setAutoDraw(true);
    }
    
    
    // *key_resp_65* updates
    if (t >= 0.0 && key_resp_65.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_65.tStart = t;  // (not accounting for frame time here)
      key_resp_65.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_65.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_65.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_65.clearEvents(); });
    }
    
    if (key_resp_65.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_65.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_65_allKeys = _key_resp_65_allKeys.concat(theseKeys);
      if (_key_resp_65_allKeys.length > 0) {
        key_resp_65.keys = _key_resp_65_allKeys[_key_resp_65_allKeys.length - 1].name;  // just the last key pressed
        key_resp_65.rt = _key_resp_65_allKeys[_key_resp_65_allKeys.length - 1].rt;
        key_resp_65.duration = _key_resp_65_allKeys[_key_resp_65_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ20Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ20RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ20' ---
    SPQ20Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ20.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_65.corr, level);
    }
    psychoJS.experiment.addData('key_resp_65.keys', key_resp_65.keys);
    if (typeof key_resp_65.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_65.rt', key_resp_65.rt);
        psychoJS.experiment.addData('key_resp_65.duration', key_resp_65.duration);
        routineTimer.reset();
        }
    
    key_resp_65.stop();
    // the Routine "SPQ20" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_66_allKeys;
var SPQ21Components;
function SPQ21RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ21' ---
    t = 0;
    SPQ21Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ21.started', globalClock.getTime());
    key_resp_66.keys = undefined;
    key_resp_66.rt = undefined;
    _key_resp_66_allKeys = [];
    // keep track of which components have finished
    SPQ21Components = [];
    SPQ21Components.push(text_213);
    SPQ21Components.push(text_214);
    SPQ21Components.push(key_resp_66);
    
    SPQ21Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ21RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ21' ---
    // get current time
    t = SPQ21Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_213* updates
    if (t >= 0.0 && text_213.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_213.tStart = t;  // (not accounting for frame time here)
      text_213.frameNStart = frameN;  // exact frame index
      
      text_213.setAutoDraw(true);
    }
    
    
    // *text_214* updates
    if (t >= 0.0 && text_214.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_214.tStart = t;  // (not accounting for frame time here)
      text_214.frameNStart = frameN;  // exact frame index
      
      text_214.setAutoDraw(true);
    }
    
    
    // *key_resp_66* updates
    if (t >= 0.0 && key_resp_66.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_66.tStart = t;  // (not accounting for frame time here)
      key_resp_66.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_66.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_66.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_66.clearEvents(); });
    }
    
    if (key_resp_66.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_66.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_66_allKeys = _key_resp_66_allKeys.concat(theseKeys);
      if (_key_resp_66_allKeys.length > 0) {
        key_resp_66.keys = _key_resp_66_allKeys[_key_resp_66_allKeys.length - 1].name;  // just the last key pressed
        key_resp_66.rt = _key_resp_66_allKeys[_key_resp_66_allKeys.length - 1].rt;
        key_resp_66.duration = _key_resp_66_allKeys[_key_resp_66_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ21Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ21RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ21' ---
    SPQ21Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ21.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_66.corr, level);
    }
    psychoJS.experiment.addData('key_resp_66.keys', key_resp_66.keys);
    if (typeof key_resp_66.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_66.rt', key_resp_66.rt);
        psychoJS.experiment.addData('key_resp_66.duration', key_resp_66.duration);
        routineTimer.reset();
        }
    
    key_resp_66.stop();
    // the Routine "SPQ21" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_67_allKeys;
var SPQ22Components;
function SPQ22RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SPQ22' ---
    t = 0;
    SPQ22Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SPQ22.started', globalClock.getTime());
    key_resp_67.keys = undefined;
    key_resp_67.rt = undefined;
    _key_resp_67_allKeys = [];
    // keep track of which components have finished
    SPQ22Components = [];
    SPQ22Components.push(text_215);
    SPQ22Components.push(text_216);
    SPQ22Components.push(key_resp_67);
    
    SPQ22Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SPQ22RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SPQ22' ---
    // get current time
    t = SPQ22Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_215* updates
    if (t >= 0.0 && text_215.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_215.tStart = t;  // (not accounting for frame time here)
      text_215.frameNStart = frameN;  // exact frame index
      
      text_215.setAutoDraw(true);
    }
    
    
    // *text_216* updates
    if (t >= 0.0 && text_216.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_216.tStart = t;  // (not accounting for frame time here)
      text_216.frameNStart = frameN;  // exact frame index
      
      text_216.setAutoDraw(true);
    }
    
    
    // *key_resp_67* updates
    if (t >= 0.0 && key_resp_67.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_67.tStart = t;  // (not accounting for frame time here)
      key_resp_67.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_67.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_67.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_67.clearEvents(); });
    }
    
    if (key_resp_67.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_67.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_67_allKeys = _key_resp_67_allKeys.concat(theseKeys);
      if (_key_resp_67_allKeys.length > 0) {
        key_resp_67.keys = _key_resp_67_allKeys[_key_resp_67_allKeys.length - 1].name;  // just the last key pressed
        key_resp_67.rt = _key_resp_67_allKeys[_key_resp_67_allKeys.length - 1].rt;
        key_resp_67.duration = _key_resp_67_allKeys[_key_resp_67_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SPQ22Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SPQ22RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SPQ22' ---
    SPQ22Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SPQ22.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_67.corr, level);
    }
    psychoJS.experiment.addData('key_resp_67.keys', key_resp_67.keys);
    if (typeof key_resp_67.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_67.rt', key_resp_67.rt);
        psychoJS.experiment.addData('key_resp_67.duration', key_resp_67.duration);
        routineTimer.reset();
        }
    
    key_resp_67.stop();
    // the Routine "SPQ22" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var q4_instructionsComponents;
function q4_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'q4_instructions' ---
    t = 0;
    q4_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('q4_instructions.started', globalClock.getTime());
    // keep track of which components have finished
    q4_instructionsComponents = [];
    q4_instructionsComponents.push(text_172);
    
    q4_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function q4_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'q4_instructions' ---
    // get current time
    t = q4_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_172* updates
    if (t >= 0.0 && text_172.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_172.tStart = t;  // (not accounting for frame time here)
      text_172.frameNStart = frameN;  // exact frame index
      
      text_172.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_172.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_172.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    q4_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function q4_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'q4_instructions' ---
    q4_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('q4_instructions.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_68_allKeys;
var SS1Components;
function SS1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS1' ---
    t = 0;
    SS1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS1.started', globalClock.getTime());
    key_resp_68.keys = undefined;
    key_resp_68.rt = undefined;
    _key_resp_68_allKeys = [];
    // keep track of which components have finished
    SS1Components = [];
    SS1Components.push(text_217);
    SS1Components.push(text_218);
    SS1Components.push(text_219);
    SS1Components.push(key_resp_68);
    
    SS1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS1' ---
    // get current time
    t = SS1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_217* updates
    if (t >= 0.0 && text_217.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_217.tStart = t;  // (not accounting for frame time here)
      text_217.frameNStart = frameN;  // exact frame index
      
      text_217.setAutoDraw(true);
    }
    
    
    // *text_218* updates
    if (t >= 0.0 && text_218.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_218.tStart = t;  // (not accounting for frame time here)
      text_218.frameNStart = frameN;  // exact frame index
      
      text_218.setAutoDraw(true);
    }
    
    
    // *text_219* updates
    if (t >= 0.0 && text_219.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_219.tStart = t;  // (not accounting for frame time here)
      text_219.frameNStart = frameN;  // exact frame index
      
      text_219.setAutoDraw(true);
    }
    
    
    // *key_resp_68* updates
    if (t >= 0.0 && key_resp_68.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_68.tStart = t;  // (not accounting for frame time here)
      key_resp_68.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_68.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_68.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_68.clearEvents(); });
    }
    
    if (key_resp_68.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_68.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_68_allKeys = _key_resp_68_allKeys.concat(theseKeys);
      if (_key_resp_68_allKeys.length > 0) {
        key_resp_68.keys = _key_resp_68_allKeys[_key_resp_68_allKeys.length - 1].name;  // just the last key pressed
        key_resp_68.rt = _key_resp_68_allKeys[_key_resp_68_allKeys.length - 1].rt;
        key_resp_68.duration = _key_resp_68_allKeys[_key_resp_68_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS1' ---
    SS1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_68.corr, level);
    }
    psychoJS.experiment.addData('key_resp_68.keys', key_resp_68.keys);
    if (typeof key_resp_68.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_68.rt', key_resp_68.rt);
        psychoJS.experiment.addData('key_resp_68.duration', key_resp_68.duration);
        routineTimer.reset();
        }
    
    key_resp_68.stop();
    // the Routine "SS1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_69_allKeys;
var SS2Components;
function SS2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS2' ---
    t = 0;
    SS2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS2.started', globalClock.getTime());
    key_resp_69.keys = undefined;
    key_resp_69.rt = undefined;
    _key_resp_69_allKeys = [];
    // keep track of which components have finished
    SS2Components = [];
    SS2Components.push(text_220);
    SS2Components.push(text_221);
    SS2Components.push(text_222);
    SS2Components.push(key_resp_69);
    
    SS2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS2' ---
    // get current time
    t = SS2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_220* updates
    if (t >= 0.0 && text_220.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_220.tStart = t;  // (not accounting for frame time here)
      text_220.frameNStart = frameN;  // exact frame index
      
      text_220.setAutoDraw(true);
    }
    
    
    // *text_221* updates
    if (t >= 0.0 && text_221.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_221.tStart = t;  // (not accounting for frame time here)
      text_221.frameNStart = frameN;  // exact frame index
      
      text_221.setAutoDraw(true);
    }
    
    
    // *text_222* updates
    if (t >= 0.0 && text_222.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_222.tStart = t;  // (not accounting for frame time here)
      text_222.frameNStart = frameN;  // exact frame index
      
      text_222.setAutoDraw(true);
    }
    
    
    // *key_resp_69* updates
    if (t >= 0.0 && key_resp_69.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_69.tStart = t;  // (not accounting for frame time here)
      key_resp_69.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_69.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_69.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_69.clearEvents(); });
    }
    
    if (key_resp_69.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_69.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_69_allKeys = _key_resp_69_allKeys.concat(theseKeys);
      if (_key_resp_69_allKeys.length > 0) {
        key_resp_69.keys = _key_resp_69_allKeys[_key_resp_69_allKeys.length - 1].name;  // just the last key pressed
        key_resp_69.rt = _key_resp_69_allKeys[_key_resp_69_allKeys.length - 1].rt;
        key_resp_69.duration = _key_resp_69_allKeys[_key_resp_69_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS2' ---
    SS2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_69.corr, level);
    }
    psychoJS.experiment.addData('key_resp_69.keys', key_resp_69.keys);
    if (typeof key_resp_69.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_69.rt', key_resp_69.rt);
        psychoJS.experiment.addData('key_resp_69.duration', key_resp_69.duration);
        routineTimer.reset();
        }
    
    key_resp_69.stop();
    // the Routine "SS2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_70_allKeys;
var SS3Components;
function SS3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS3' ---
    t = 0;
    SS3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS3.started', globalClock.getTime());
    key_resp_70.keys = undefined;
    key_resp_70.rt = undefined;
    _key_resp_70_allKeys = [];
    // keep track of which components have finished
    SS3Components = [];
    SS3Components.push(text_223);
    SS3Components.push(text_224);
    SS3Components.push(text_225);
    SS3Components.push(key_resp_70);
    
    SS3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS3' ---
    // get current time
    t = SS3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_223* updates
    if (t >= 0.0 && text_223.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_223.tStart = t;  // (not accounting for frame time here)
      text_223.frameNStart = frameN;  // exact frame index
      
      text_223.setAutoDraw(true);
    }
    
    
    // *text_224* updates
    if (t >= 0.0 && text_224.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_224.tStart = t;  // (not accounting for frame time here)
      text_224.frameNStart = frameN;  // exact frame index
      
      text_224.setAutoDraw(true);
    }
    
    
    // *text_225* updates
    if (t >= 0.0 && text_225.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_225.tStart = t;  // (not accounting for frame time here)
      text_225.frameNStart = frameN;  // exact frame index
      
      text_225.setAutoDraw(true);
    }
    
    
    // *key_resp_70* updates
    if (t >= 0.0 && key_resp_70.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_70.tStart = t;  // (not accounting for frame time here)
      key_resp_70.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_70.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_70.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_70.clearEvents(); });
    }
    
    if (key_resp_70.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_70.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_70_allKeys = _key_resp_70_allKeys.concat(theseKeys);
      if (_key_resp_70_allKeys.length > 0) {
        key_resp_70.keys = _key_resp_70_allKeys[_key_resp_70_allKeys.length - 1].name;  // just the last key pressed
        key_resp_70.rt = _key_resp_70_allKeys[_key_resp_70_allKeys.length - 1].rt;
        key_resp_70.duration = _key_resp_70_allKeys[_key_resp_70_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS3' ---
    SS3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_70.corr, level);
    }
    psychoJS.experiment.addData('key_resp_70.keys', key_resp_70.keys);
    if (typeof key_resp_70.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_70.rt', key_resp_70.rt);
        psychoJS.experiment.addData('key_resp_70.duration', key_resp_70.duration);
        routineTimer.reset();
        }
    
    key_resp_70.stop();
    // the Routine "SS3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_71_allKeys;
var SS4Components;
function SS4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS4' ---
    t = 0;
    SS4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS4.started', globalClock.getTime());
    key_resp_71.keys = undefined;
    key_resp_71.rt = undefined;
    _key_resp_71_allKeys = [];
    // keep track of which components have finished
    SS4Components = [];
    SS4Components.push(text_226);
    SS4Components.push(text_227);
    SS4Components.push(text_228);
    SS4Components.push(key_resp_71);
    
    SS4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS4' ---
    // get current time
    t = SS4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_226* updates
    if (t >= 0.0 && text_226.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_226.tStart = t;  // (not accounting for frame time here)
      text_226.frameNStart = frameN;  // exact frame index
      
      text_226.setAutoDraw(true);
    }
    
    
    // *text_227* updates
    if (t >= 0.0 && text_227.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_227.tStart = t;  // (not accounting for frame time here)
      text_227.frameNStart = frameN;  // exact frame index
      
      text_227.setAutoDraw(true);
    }
    
    
    // *text_228* updates
    if (t >= 0.0 && text_228.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_228.tStart = t;  // (not accounting for frame time here)
      text_228.frameNStart = frameN;  // exact frame index
      
      text_228.setAutoDraw(true);
    }
    
    
    // *key_resp_71* updates
    if (t >= 0.0 && key_resp_71.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_71.tStart = t;  // (not accounting for frame time here)
      key_resp_71.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_71.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_71.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_71.clearEvents(); });
    }
    
    if (key_resp_71.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_71.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_71_allKeys = _key_resp_71_allKeys.concat(theseKeys);
      if (_key_resp_71_allKeys.length > 0) {
        key_resp_71.keys = _key_resp_71_allKeys[_key_resp_71_allKeys.length - 1].name;  // just the last key pressed
        key_resp_71.rt = _key_resp_71_allKeys[_key_resp_71_allKeys.length - 1].rt;
        key_resp_71.duration = _key_resp_71_allKeys[_key_resp_71_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS4' ---
    SS4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_71.corr, level);
    }
    psychoJS.experiment.addData('key_resp_71.keys', key_resp_71.keys);
    if (typeof key_resp_71.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_71.rt', key_resp_71.rt);
        psychoJS.experiment.addData('key_resp_71.duration', key_resp_71.duration);
        routineTimer.reset();
        }
    
    key_resp_71.stop();
    // the Routine "SS4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_72_allKeys;
var SS5Components;
function SS5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS5' ---
    t = 0;
    SS5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS5.started', globalClock.getTime());
    key_resp_72.keys = undefined;
    key_resp_72.rt = undefined;
    _key_resp_72_allKeys = [];
    // keep track of which components have finished
    SS5Components = [];
    SS5Components.push(text_229);
    SS5Components.push(text_230);
    SS5Components.push(text_231);
    SS5Components.push(key_resp_72);
    
    SS5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS5' ---
    // get current time
    t = SS5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_229* updates
    if (t >= 0.0 && text_229.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_229.tStart = t;  // (not accounting for frame time here)
      text_229.frameNStart = frameN;  // exact frame index
      
      text_229.setAutoDraw(true);
    }
    
    
    // *text_230* updates
    if (t >= 0.0 && text_230.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_230.tStart = t;  // (not accounting for frame time here)
      text_230.frameNStart = frameN;  // exact frame index
      
      text_230.setAutoDraw(true);
    }
    
    
    // *text_231* updates
    if (t >= 0.0 && text_231.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_231.tStart = t;  // (not accounting for frame time here)
      text_231.frameNStart = frameN;  // exact frame index
      
      text_231.setAutoDraw(true);
    }
    
    
    // *key_resp_72* updates
    if (t >= 0.0 && key_resp_72.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_72.tStart = t;  // (not accounting for frame time here)
      key_resp_72.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_72.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_72.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_72.clearEvents(); });
    }
    
    if (key_resp_72.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_72.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_72_allKeys = _key_resp_72_allKeys.concat(theseKeys);
      if (_key_resp_72_allKeys.length > 0) {
        key_resp_72.keys = _key_resp_72_allKeys[_key_resp_72_allKeys.length - 1].name;  // just the last key pressed
        key_resp_72.rt = _key_resp_72_allKeys[_key_resp_72_allKeys.length - 1].rt;
        key_resp_72.duration = _key_resp_72_allKeys[_key_resp_72_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS5' ---
    SS5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_72.corr, level);
    }
    psychoJS.experiment.addData('key_resp_72.keys', key_resp_72.keys);
    if (typeof key_resp_72.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_72.rt', key_resp_72.rt);
        psychoJS.experiment.addData('key_resp_72.duration', key_resp_72.duration);
        routineTimer.reset();
        }
    
    key_resp_72.stop();
    // the Routine "SS5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_73_allKeys;
var SS6Components;
function SS6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS6' ---
    t = 0;
    SS6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS6.started', globalClock.getTime());
    key_resp_73.keys = undefined;
    key_resp_73.rt = undefined;
    _key_resp_73_allKeys = [];
    // keep track of which components have finished
    SS6Components = [];
    SS6Components.push(text_232);
    SS6Components.push(text_233);
    SS6Components.push(text_234);
    SS6Components.push(key_resp_73);
    
    SS6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS6' ---
    // get current time
    t = SS6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_232* updates
    if (t >= 0.0 && text_232.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_232.tStart = t;  // (not accounting for frame time here)
      text_232.frameNStart = frameN;  // exact frame index
      
      text_232.setAutoDraw(true);
    }
    
    
    // *text_233* updates
    if (t >= 0.0 && text_233.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_233.tStart = t;  // (not accounting for frame time here)
      text_233.frameNStart = frameN;  // exact frame index
      
      text_233.setAutoDraw(true);
    }
    
    
    // *text_234* updates
    if (t >= 0.0 && text_234.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_234.tStart = t;  // (not accounting for frame time here)
      text_234.frameNStart = frameN;  // exact frame index
      
      text_234.setAutoDraw(true);
    }
    
    
    // *key_resp_73* updates
    if (t >= 0.0 && key_resp_73.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_73.tStart = t;  // (not accounting for frame time here)
      key_resp_73.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_73.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_73.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_73.clearEvents(); });
    }
    
    if (key_resp_73.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_73.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_73_allKeys = _key_resp_73_allKeys.concat(theseKeys);
      if (_key_resp_73_allKeys.length > 0) {
        key_resp_73.keys = _key_resp_73_allKeys[_key_resp_73_allKeys.length - 1].name;  // just the last key pressed
        key_resp_73.rt = _key_resp_73_allKeys[_key_resp_73_allKeys.length - 1].rt;
        key_resp_73.duration = _key_resp_73_allKeys[_key_resp_73_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS6' ---
    SS6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS6.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_73.corr, level);
    }
    psychoJS.experiment.addData('key_resp_73.keys', key_resp_73.keys);
    if (typeof key_resp_73.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_73.rt', key_resp_73.rt);
        psychoJS.experiment.addData('key_resp_73.duration', key_resp_73.duration);
        routineTimer.reset();
        }
    
    key_resp_73.stop();
    // the Routine "SS6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_74_allKeys;
var SS7Components;
function SS7RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS7' ---
    t = 0;
    SS7Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS7.started', globalClock.getTime());
    key_resp_74.keys = undefined;
    key_resp_74.rt = undefined;
    _key_resp_74_allKeys = [];
    // keep track of which components have finished
    SS7Components = [];
    SS7Components.push(text_235);
    SS7Components.push(text_236);
    SS7Components.push(text_237);
    SS7Components.push(key_resp_74);
    
    SS7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS7RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS7' ---
    // get current time
    t = SS7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_235* updates
    if (t >= 0.0 && text_235.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_235.tStart = t;  // (not accounting for frame time here)
      text_235.frameNStart = frameN;  // exact frame index
      
      text_235.setAutoDraw(true);
    }
    
    
    // *text_236* updates
    if (t >= 0.0 && text_236.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_236.tStart = t;  // (not accounting for frame time here)
      text_236.frameNStart = frameN;  // exact frame index
      
      text_236.setAutoDraw(true);
    }
    
    
    // *text_237* updates
    if (t >= 0.0 && text_237.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_237.tStart = t;  // (not accounting for frame time here)
      text_237.frameNStart = frameN;  // exact frame index
      
      text_237.setAutoDraw(true);
    }
    
    
    // *key_resp_74* updates
    if (t >= 0.0 && key_resp_74.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_74.tStart = t;  // (not accounting for frame time here)
      key_resp_74.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_74.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_74.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_74.clearEvents(); });
    }
    
    if (key_resp_74.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_74.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_74_allKeys = _key_resp_74_allKeys.concat(theseKeys);
      if (_key_resp_74_allKeys.length > 0) {
        key_resp_74.keys = _key_resp_74_allKeys[_key_resp_74_allKeys.length - 1].name;  // just the last key pressed
        key_resp_74.rt = _key_resp_74_allKeys[_key_resp_74_allKeys.length - 1].rt;
        key_resp_74.duration = _key_resp_74_allKeys[_key_resp_74_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS7RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS7' ---
    SS7Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS7.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_74.corr, level);
    }
    psychoJS.experiment.addData('key_resp_74.keys', key_resp_74.keys);
    if (typeof key_resp_74.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_74.rt', key_resp_74.rt);
        psychoJS.experiment.addData('key_resp_74.duration', key_resp_74.duration);
        routineTimer.reset();
        }
    
    key_resp_74.stop();
    // the Routine "SS7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_75_allKeys;
var SS8Components;
function SS8RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS8' ---
    t = 0;
    SS8Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS8.started', globalClock.getTime());
    key_resp_75.keys = undefined;
    key_resp_75.rt = undefined;
    _key_resp_75_allKeys = [];
    // keep track of which components have finished
    SS8Components = [];
    SS8Components.push(text_238);
    SS8Components.push(text_239);
    SS8Components.push(text_240);
    SS8Components.push(key_resp_75);
    
    SS8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS8RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS8' ---
    // get current time
    t = SS8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_238* updates
    if (t >= 0.0 && text_238.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_238.tStart = t;  // (not accounting for frame time here)
      text_238.frameNStart = frameN;  // exact frame index
      
      text_238.setAutoDraw(true);
    }
    
    
    // *text_239* updates
    if (t >= 0.0 && text_239.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_239.tStart = t;  // (not accounting for frame time here)
      text_239.frameNStart = frameN;  // exact frame index
      
      text_239.setAutoDraw(true);
    }
    
    
    // *text_240* updates
    if (t >= 0.0 && text_240.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_240.tStart = t;  // (not accounting for frame time here)
      text_240.frameNStart = frameN;  // exact frame index
      
      text_240.setAutoDraw(true);
    }
    
    
    // *key_resp_75* updates
    if (t >= 0.0 && key_resp_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_75.tStart = t;  // (not accounting for frame time here)
      key_resp_75.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_75.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_75.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_75.clearEvents(); });
    }
    
    if (key_resp_75.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_75.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_75_allKeys = _key_resp_75_allKeys.concat(theseKeys);
      if (_key_resp_75_allKeys.length > 0) {
        key_resp_75.keys = _key_resp_75_allKeys[_key_resp_75_allKeys.length - 1].name;  // just the last key pressed
        key_resp_75.rt = _key_resp_75_allKeys[_key_resp_75_allKeys.length - 1].rt;
        key_resp_75.duration = _key_resp_75_allKeys[_key_resp_75_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS8RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS8' ---
    SS8Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS8.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_75.corr, level);
    }
    psychoJS.experiment.addData('key_resp_75.keys', key_resp_75.keys);
    if (typeof key_resp_75.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_75.rt', key_resp_75.rt);
        psychoJS.experiment.addData('key_resp_75.duration', key_resp_75.duration);
        routineTimer.reset();
        }
    
    key_resp_75.stop();
    // the Routine "SS8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_76_allKeys;
var SS9Components;
function SS9RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS9' ---
    t = 0;
    SS9Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS9.started', globalClock.getTime());
    key_resp_76.keys = undefined;
    key_resp_76.rt = undefined;
    _key_resp_76_allKeys = [];
    // keep track of which components have finished
    SS9Components = [];
    SS9Components.push(text_241);
    SS9Components.push(text_242);
    SS9Components.push(text_243);
    SS9Components.push(key_resp_76);
    
    SS9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS9RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS9' ---
    // get current time
    t = SS9Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_241* updates
    if (t >= 0.0 && text_241.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_241.tStart = t;  // (not accounting for frame time here)
      text_241.frameNStart = frameN;  // exact frame index
      
      text_241.setAutoDraw(true);
    }
    
    
    // *text_242* updates
    if (t >= 0.0 && text_242.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_242.tStart = t;  // (not accounting for frame time here)
      text_242.frameNStart = frameN;  // exact frame index
      
      text_242.setAutoDraw(true);
    }
    
    
    // *text_243* updates
    if (t >= 0.0 && text_243.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_243.tStart = t;  // (not accounting for frame time here)
      text_243.frameNStart = frameN;  // exact frame index
      
      text_243.setAutoDraw(true);
    }
    
    
    // *key_resp_76* updates
    if (t >= 0.0 && key_resp_76.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_76.tStart = t;  // (not accounting for frame time here)
      key_resp_76.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_76.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_76.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_76.clearEvents(); });
    }
    
    if (key_resp_76.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_76.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_76_allKeys = _key_resp_76_allKeys.concat(theseKeys);
      if (_key_resp_76_allKeys.length > 0) {
        key_resp_76.keys = _key_resp_76_allKeys[_key_resp_76_allKeys.length - 1].name;  // just the last key pressed
        key_resp_76.rt = _key_resp_76_allKeys[_key_resp_76_allKeys.length - 1].rt;
        key_resp_76.duration = _key_resp_76_allKeys[_key_resp_76_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS9Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS9RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS9' ---
    SS9Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS9.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_76.corr, level);
    }
    psychoJS.experiment.addData('key_resp_76.keys', key_resp_76.keys);
    if (typeof key_resp_76.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_76.rt', key_resp_76.rt);
        psychoJS.experiment.addData('key_resp_76.duration', key_resp_76.duration);
        routineTimer.reset();
        }
    
    key_resp_76.stop();
    // the Routine "SS9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_77_allKeys;
var SS10Components;
function SS10RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SS10' ---
    t = 0;
    SS10Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('SS10.started', globalClock.getTime());
    key_resp_77.keys = undefined;
    key_resp_77.rt = undefined;
    _key_resp_77_allKeys = [];
    // keep track of which components have finished
    SS10Components = [];
    SS10Components.push(text_244);
    SS10Components.push(text_245);
    SS10Components.push(text_246);
    SS10Components.push(key_resp_77);
    
    SS10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function SS10RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SS10' ---
    // get current time
    t = SS10Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_244* updates
    if (t >= 0.0 && text_244.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_244.tStart = t;  // (not accounting for frame time here)
      text_244.frameNStart = frameN;  // exact frame index
      
      text_244.setAutoDraw(true);
    }
    
    
    // *text_245* updates
    if (t >= 0.0 && text_245.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_245.tStart = t;  // (not accounting for frame time here)
      text_245.frameNStart = frameN;  // exact frame index
      
      text_245.setAutoDraw(true);
    }
    
    
    // *text_246* updates
    if (t >= 0.0 && text_246.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_246.tStart = t;  // (not accounting for frame time here)
      text_246.frameNStart = frameN;  // exact frame index
      
      text_246.setAutoDraw(true);
    }
    
    
    // *key_resp_77* updates
    if (t >= 0.0 && key_resp_77.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_77.tStart = t;  // (not accounting for frame time here)
      key_resp_77.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_77.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_77.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_77.clearEvents(); });
    }
    
    if (key_resp_77.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_77.getKeys({keyList: [1, 2, 3, 4, 5, '1', '2', '3', '4', '5'], waitRelease: false});
      _key_resp_77_allKeys = _key_resp_77_allKeys.concat(theseKeys);
      if (_key_resp_77_allKeys.length > 0) {
        key_resp_77.keys = _key_resp_77_allKeys[_key_resp_77_allKeys.length - 1].name;  // just the last key pressed
        key_resp_77.rt = _key_resp_77_allKeys[_key_resp_77_allKeys.length - 1].rt;
        key_resp_77.duration = _key_resp_77_allKeys[_key_resp_77_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    SS10Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SS10RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SS10' ---
    SS10Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SS10.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_77.corr, level);
    }
    psychoJS.experiment.addData('key_resp_77.keys', key_resp_77.keys);
    if (typeof key_resp_77.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_77.rt', key_resp_77.rt);
        psychoJS.experiment.addData('key_resp_77.duration', key_resp_77.duration);
        routineTimer.reset();
        }
    
    key_resp_77.stop();
    // the Routine "SS10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructions_get_right;
function instructions_get_rightLoopBegin(instructions_get_rightLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    instructions_get_right = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 500, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'instructions_get_right'
    });
    psychoJS.experiment.addLoop(instructions_get_right); // add the loop to the experiment
    currentLoop = instructions_get_right;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    instructions_get_right.forEach(function() {
      snapshot = instructions_get_right.getSnapshot();
    
      instructions_get_rightLoopScheduler.add(importConditions(snapshot));
      instructions_get_rightLoopScheduler.add(instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instructionsRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(second_instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(second_instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(second_instructionsRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(third_instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(third_instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(third_instructionsRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructions4RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instructions4RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instructions4RoutineEnd(snapshot));
      const practice_loopLoopScheduler = new Scheduler(psychoJS);
      instructions_get_rightLoopScheduler.add(practice_loopLoopBegin(practice_loopLoopScheduler, snapshot));
      instructions_get_rightLoopScheduler.add(practice_loopLoopScheduler);
      instructions_get_rightLoopScheduler.add(practice_loopLoopEnd);
      instructions_get_rightLoopScheduler.add(memory_quiz_instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(memory_quiz_instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(memory_quiz_instructionsRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(quiz1_iRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(quiz1_iRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(quiz1_iRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(quiz2_iRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(quiz2_iRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(quiz2_iRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(quiz3RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(quiz3RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(quiz3RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(quiz4RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(quiz4RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(quiz4RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(quiz_feedbackRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(quiz_feedbackRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(quiz_feedbackRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_get_rightLoopEndIteration(instructions_get_rightLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var practice_loop;
function practice_loopLoopBegin(practice_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 500, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'practice_loop'
    });
    psychoJS.experiment.addLoop(practice_loop); // add the loop to the experiment
    currentLoop = practice_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practice_loop.forEach(function() {
      snapshot = practice_loop.getSnapshot();
    
      practice_loopLoopScheduler.add(importConditions(snapshot));
      const practice_trialsLoopScheduler = new Scheduler(psychoJS);
      practice_loopLoopScheduler.add(practice_trialsLoopBegin(practice_trialsLoopScheduler, snapshot));
      practice_loopLoopScheduler.add(practice_trialsLoopScheduler);
      practice_loopLoopScheduler.add(practice_trialsLoopEnd);
      practice_loopLoopScheduler.add(practice1_quizRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(practice1_quizRoutineEachFrame());
      practice_loopLoopScheduler.add(practice1_quizRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(practice1_quizfeedbackRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(practice1_quizfeedbackRoutineEachFrame());
      practice_loopLoopScheduler.add(practice1_quizfeedbackRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(practice_loopLoopEndIteration(practice_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var practice_trials;
function practice_trialsLoopBegin(practice_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stage2_4_practice.csv',
      seed: undefined, name: 'practice_trials'
    });
    psychoJS.experiment.addLoop(practice_trials); // add the loop to the experiment
    currentLoop = practice_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practice_trials.forEach(function() {
      snapshot = practice_trials.getSnapshot();
    
      practice_trialsLoopScheduler.add(importConditions(snapshot));
      practice_trialsLoopScheduler.add(practice1RoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(practice1RoutineEachFrame());
      practice_trialsLoopScheduler.add(practice1RoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice1_resultRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(practice1_resultRoutineEachFrame());
      practice_trialsLoopScheduler.add(practice1_resultRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(next_trialRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(next_trialRoutineEachFrame());
      practice_trialsLoopScheduler.add(next_trialRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice_trialsLoopEndIteration(practice_trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practice_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function practice_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function instructions_get_rightLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(instructions_get_right);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function instructions_get_rightLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var learning_phase;
function learning_phaseLoopBegin(learning_phaseLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    learning_phase = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'learning_phase'
    });
    psychoJS.experiment.addLoop(learning_phase); // add the loop to the experiment
    currentLoop = learning_phase;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    learning_phase.forEach(function() {
      snapshot = learning_phase.getSnapshot();
    
      learning_phaseLoopScheduler.add(importConditions(snapshot));
      const learn_1LoopScheduler = new Scheduler(psychoJS);
      learning_phaseLoopScheduler.add(learn_1LoopBegin(learn_1LoopScheduler, snapshot));
      learning_phaseLoopScheduler.add(learn_1LoopScheduler);
      learning_phaseLoopScheduler.add(learn_1LoopEnd);
      learning_phaseLoopScheduler.add(counter_quizzes_roundRoutineBegin(snapshot));
      learning_phaseLoopScheduler.add(counter_quizzes_roundRoutineEachFrame());
      learning_phaseLoopScheduler.add(counter_quizzes_roundRoutineEnd(snapshot));
      learning_phaseLoopScheduler.add(betweenRoutineBegin(snapshot));
      learning_phaseLoopScheduler.add(betweenRoutineEachFrame());
      learning_phaseLoopScheduler.add(betweenRoutineEnd(snapshot));
      const quiz_loop1LoopScheduler = new Scheduler(psychoJS);
      learning_phaseLoopScheduler.add(quiz_loop1LoopBegin(quiz_loop1LoopScheduler, snapshot));
      learning_phaseLoopScheduler.add(quiz_loop1LoopScheduler);
      learning_phaseLoopScheduler.add(quiz_loop1LoopEnd);
      learning_phaseLoopScheduler.add(back_to_learnRoutineBegin(snapshot));
      learning_phaseLoopScheduler.add(back_to_learnRoutineEachFrame());
      learning_phaseLoopScheduler.add(back_to_learnRoutineEnd(snapshot));
      const learn_1_2LoopScheduler = new Scheduler(psychoJS);
      learning_phaseLoopScheduler.add(learn_1_2LoopBegin(learn_1_2LoopScheduler, snapshot));
      learning_phaseLoopScheduler.add(learn_1_2LoopScheduler);
      learning_phaseLoopScheduler.add(learn_1_2LoopEnd);
      learning_phaseLoopScheduler.add(betweenRoutineBegin(snapshot));
      learning_phaseLoopScheduler.add(betweenRoutineEachFrame());
      learning_phaseLoopScheduler.add(betweenRoutineEnd(snapshot));
      const quizloop2LoopScheduler = new Scheduler(psychoJS);
      learning_phaseLoopScheduler.add(quizloop2LoopBegin(quizloop2LoopScheduler, snapshot));
      learning_phaseLoopScheduler.add(quizloop2LoopScheduler);
      learning_phaseLoopScheduler.add(quizloop2LoopEnd);
      learning_phaseLoopScheduler.add(planning_pathsRoutineBegin(snapshot));
      learning_phaseLoopScheduler.add(planning_pathsRoutineEachFrame());
      learning_phaseLoopScheduler.add(planning_pathsRoutineEnd(snapshot));
      const planning_during_trainingLoopScheduler = new Scheduler(psychoJS);
      learning_phaseLoopScheduler.add(planning_during_trainingLoopBegin(planning_during_trainingLoopScheduler, snapshot));
      learning_phaseLoopScheduler.add(planning_during_trainingLoopScheduler);
      learning_phaseLoopScheduler.add(planning_during_trainingLoopEnd);
      learning_phaseLoopScheduler.add(total_score_planningRoutineBegin(snapshot));
      learning_phaseLoopScheduler.add(total_score_planningRoutineEachFrame());
      learning_phaseLoopScheduler.add(total_score_planningRoutineEnd(snapshot));
      learning_phaseLoopScheduler.add(learning_phaseLoopEndIteration(learning_phaseLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var learn_1;
function learn_1LoopBegin(learn_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    learn_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'image_train_press.xlsx',
      seed: undefined, name: 'learn_1'
    });
    psychoJS.experiment.addLoop(learn_1); // add the loop to the experiment
    currentLoop = learn_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    learn_1.forEach(function() {
      snapshot = learn_1.getSnapshot();
    
      learn_1LoopScheduler.add(importConditions(snapshot));
      const incorrect_loopLoopScheduler = new Scheduler(psychoJS);
      learn_1LoopScheduler.add(incorrect_loopLoopBegin(incorrect_loopLoopScheduler, snapshot));
      learn_1LoopScheduler.add(incorrect_loopLoopScheduler);
      learn_1LoopScheduler.add(incorrect_loopLoopEnd);
      learn_1LoopScheduler.add(learn2RoutineBegin(snapshot));
      learn_1LoopScheduler.add(learn2RoutineEachFrame());
      learn_1LoopScheduler.add(learn2RoutineEnd(snapshot));
      learn_1LoopScheduler.add(next_trialRoutineBegin(snapshot));
      learn_1LoopScheduler.add(next_trialRoutineEachFrame());
      learn_1LoopScheduler.add(next_trialRoutineEnd(snapshot));
      learn_1LoopScheduler.add(learn_1LoopEndIteration(learn_1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var incorrect_loop;
function incorrect_loopLoopBegin(incorrect_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    incorrect_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 9999, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'incorrect_loop'
    });
    psychoJS.experiment.addLoop(incorrect_loop); // add the loop to the experiment
    currentLoop = incorrect_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    incorrect_loop.forEach(function() {
      snapshot = incorrect_loop.getSnapshot();
    
      incorrect_loopLoopScheduler.add(importConditions(snapshot));
      incorrect_loopLoopScheduler.add(learn1RoutineBegin(snapshot));
      incorrect_loopLoopScheduler.add(learn1RoutineEachFrame());
      incorrect_loopLoopScheduler.add(learn1RoutineEnd(snapshot));
      incorrect_loopLoopScheduler.add(check_incorrect1RoutineBegin(snapshot));
      incorrect_loopLoopScheduler.add(check_incorrect1RoutineEachFrame());
      incorrect_loopLoopScheduler.add(check_incorrect1RoutineEnd(snapshot));
      incorrect_loopLoopScheduler.add(incorrect_loopLoopEndIteration(incorrect_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function incorrect_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(incorrect_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function incorrect_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function learn_1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(learn_1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function learn_1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var quiz_loop1;
function quiz_loop1LoopBegin(quiz_loop1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    quiz_loop1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'quiz_1.xlsx',
      seed: undefined, name: 'quiz_loop1'
    });
    psychoJS.experiment.addLoop(quiz_loop1); // add the loop to the experiment
    currentLoop = quiz_loop1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    quiz_loop1.forEach(function() {
      snapshot = quiz_loop1.getSnapshot();
    
      quiz_loop1LoopScheduler.add(importConditions(snapshot));
      quiz_loop1LoopScheduler.add(quizRoutineBegin(snapshot));
      quiz_loop1LoopScheduler.add(quizRoutineEachFrame());
      quiz_loop1LoopScheduler.add(quizRoutineEnd(snapshot));
      quiz_loop1LoopScheduler.add(quiz_feedbackRoutineBegin(snapshot));
      quiz_loop1LoopScheduler.add(quiz_feedbackRoutineEachFrame());
      quiz_loop1LoopScheduler.add(quiz_feedbackRoutineEnd(snapshot));
      quiz_loop1LoopScheduler.add(quiz_loop1LoopEndIteration(quiz_loop1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function quiz_loop1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(quiz_loop1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function quiz_loop1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var learn_1_2;
function learn_1_2LoopBegin(learn_1_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    learn_1_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'image_train_press.xlsx',
      seed: undefined, name: 'learn_1_2'
    });
    psychoJS.experiment.addLoop(learn_1_2); // add the loop to the experiment
    currentLoop = learn_1_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    learn_1_2.forEach(function() {
      snapshot = learn_1_2.getSnapshot();
    
      learn_1_2LoopScheduler.add(importConditions(snapshot));
      const incorrect_loop2LoopScheduler = new Scheduler(psychoJS);
      learn_1_2LoopScheduler.add(incorrect_loop2LoopBegin(incorrect_loop2LoopScheduler, snapshot));
      learn_1_2LoopScheduler.add(incorrect_loop2LoopScheduler);
      learn_1_2LoopScheduler.add(incorrect_loop2LoopEnd);
      learn_1_2LoopScheduler.add(learn2RoutineBegin(snapshot));
      learn_1_2LoopScheduler.add(learn2RoutineEachFrame());
      learn_1_2LoopScheduler.add(learn2RoutineEnd(snapshot));
      learn_1_2LoopScheduler.add(next_trialRoutineBegin(snapshot));
      learn_1_2LoopScheduler.add(next_trialRoutineEachFrame());
      learn_1_2LoopScheduler.add(next_trialRoutineEnd(snapshot));
      learn_1_2LoopScheduler.add(learn_1_2LoopEndIteration(learn_1_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var incorrect_loop2;
function incorrect_loop2LoopBegin(incorrect_loop2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    incorrect_loop2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 9999, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'incorrect_loop2'
    });
    psychoJS.experiment.addLoop(incorrect_loop2); // add the loop to the experiment
    currentLoop = incorrect_loop2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    incorrect_loop2.forEach(function() {
      snapshot = incorrect_loop2.getSnapshot();
    
      incorrect_loop2LoopScheduler.add(importConditions(snapshot));
      incorrect_loop2LoopScheduler.add(learn1RoutineBegin(snapshot));
      incorrect_loop2LoopScheduler.add(learn1RoutineEachFrame());
      incorrect_loop2LoopScheduler.add(learn1RoutineEnd(snapshot));
      incorrect_loop2LoopScheduler.add(check_incorrectRoutineBegin(snapshot));
      incorrect_loop2LoopScheduler.add(check_incorrectRoutineEachFrame());
      incorrect_loop2LoopScheduler.add(check_incorrectRoutineEnd(snapshot));
      incorrect_loop2LoopScheduler.add(incorrect_loop2LoopEndIteration(incorrect_loop2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function incorrect_loop2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(incorrect_loop2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function incorrect_loop2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function learn_1_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(learn_1_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function learn_1_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var quizloop2;
function quizloop2LoopBegin(quizloop2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    quizloop2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'quiz_1.xlsx',
      seed: undefined, name: 'quizloop2'
    });
    psychoJS.experiment.addLoop(quizloop2); // add the loop to the experiment
    currentLoop = quizloop2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    quizloop2.forEach(function() {
      snapshot = quizloop2.getSnapshot();
    
      quizloop2LoopScheduler.add(importConditions(snapshot));
      quizloop2LoopScheduler.add(quiz2RoutineBegin(snapshot));
      quizloop2LoopScheduler.add(quiz2RoutineEachFrame());
      quizloop2LoopScheduler.add(quiz2RoutineEnd(snapshot));
      quizloop2LoopScheduler.add(quiz_feedbackRoutineBegin(snapshot));
      quizloop2LoopScheduler.add(quiz_feedbackRoutineEachFrame());
      quizloop2LoopScheduler.add(quiz_feedbackRoutineEnd(snapshot));
      quizloop2LoopScheduler.add(quizloop2LoopEndIteration(quizloop2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function quizloop2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(quizloop2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function quizloop2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var planning_during_training;
function planning_during_trainingLoopBegin(planning_during_trainingLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    planning_during_training = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'forgetting1.xlsx',
      seed: undefined, name: 'planning_during_training'
    });
    psychoJS.experiment.addLoop(planning_during_training); // add the loop to the experiment
    currentLoop = planning_during_training;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    planning_during_training.forEach(function() {
      snapshot = planning_during_training.getSnapshot();
    
      planning_during_trainingLoopScheduler.add(importConditions(snapshot));
      planning_during_trainingLoopScheduler.add(forgetting_paths1RoutineBegin(snapshot));
      planning_during_trainingLoopScheduler.add(forgetting_paths1RoutineEachFrame());
      planning_during_trainingLoopScheduler.add(forgetting_paths1RoutineEnd(snapshot));
      planning_during_trainingLoopScheduler.add(planningpathstraining2RoutineBegin(snapshot));
      planning_during_trainingLoopScheduler.add(planningpathstraining2RoutineEachFrame());
      planning_during_trainingLoopScheduler.add(planningpathstraining2RoutineEnd(snapshot));
      planning_during_trainingLoopScheduler.add(correct_forget_pathsRoutineBegin(snapshot));
      planning_during_trainingLoopScheduler.add(correct_forget_pathsRoutineEachFrame());
      planning_during_trainingLoopScheduler.add(correct_forget_pathsRoutineEnd(snapshot));
      planning_during_trainingLoopScheduler.add(planning_during_trainingLoopEndIteration(planning_during_trainingLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function planning_during_trainingLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(planning_during_training);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function planning_during_trainingLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function learning_phaseLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(learning_phase);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function learning_phaseLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var instructions_planning_get_right;
function instructions_planning_get_rightLoopBegin(instructions_planning_get_rightLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    instructions_planning_get_right = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 999, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'instructions_planning_get_right'
    });
    psychoJS.experiment.addLoop(instructions_planning_get_right); // add the loop to the experiment
    currentLoop = instructions_planning_get_right;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    instructions_planning_get_right.forEach(function() {
      snapshot = instructions_planning_get_right.getSnapshot();
    
      instructions_planning_get_rightLoopScheduler.add(importConditions(snapshot));
      instructions_planning_get_rightLoopScheduler.add(instructions_rewardRoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(instructions_rewardRoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(instructions_rewardRoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(instructions_planning_2RoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(instructions_planning_2RoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(instructions_planning_2RoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(instructions_example_trialRoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(instructions_example_trialRoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(instructions_example_trialRoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(long_term_reward_instructionsRoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(long_term_reward_instructionsRoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(long_term_reward_instructionsRoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_1RoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_1RoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_1RoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_2RoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_2RoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_2RoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_3RoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_3RoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(quiz_planning_3RoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_feedbackRoutineBegin(snapshot));
      instructions_planning_get_rightLoopScheduler.add(quiz_feedbackRoutineEachFrame());
      instructions_planning_get_rightLoopScheduler.add(quiz_feedbackRoutineEnd(snapshot));
      instructions_planning_get_rightLoopScheduler.add(instructions_planning_get_rightLoopEndIteration(instructions_planning_get_rightLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function instructions_planning_get_rightLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(instructions_planning_get_right);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function instructions_planning_get_rightLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var planning_loop;
function planning_loopLoopBegin(planning_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    planning_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'planning_trials.xlsx',
      seed: undefined, name: 'planning_loop'
    });
    psychoJS.experiment.addLoop(planning_loop); // add the loop to the experiment
    currentLoop = planning_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    planning_loop.forEach(function() {
      snapshot = planning_loop.getSnapshot();
    
      planning_loopLoopScheduler.add(importConditions(snapshot));
      planning_loopLoopScheduler.add(plan1_info_2RoutineBegin(snapshot));
      planning_loopLoopScheduler.add(plan1_info_2RoutineEachFrame());
      planning_loopLoopScheduler.add(plan1_info_2RoutineEnd(snapshot));
      planning_loopLoopScheduler.add(plan2_infoRoutineBegin(snapshot));
      planning_loopLoopScheduler.add(plan2_infoRoutineEachFrame());
      planning_loopLoopScheduler.add(plan2_infoRoutineEnd(snapshot));
      planning_loopLoopScheduler.add(plan3_infoRoutineBegin(snapshot));
      planning_loopLoopScheduler.add(plan3_infoRoutineEachFrame());
      planning_loopLoopScheduler.add(plan3_infoRoutineEnd(snapshot));
      planning_loopLoopScheduler.add(planning4RoutineBegin(snapshot));
      planning_loopLoopScheduler.add(planning4RoutineEachFrame());
      planning_loopLoopScheduler.add(planning4RoutineEnd(snapshot));
      planning_loopLoopScheduler.add(next_trialRoutineBegin(snapshot));
      planning_loopLoopScheduler.add(next_trialRoutineEachFrame());
      planning_loopLoopScheduler.add(next_trialRoutineEnd(snapshot));
      planning_loopLoopScheduler.add(planning_loopLoopEndIteration(planning_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function planning_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(planning_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function planning_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var remember_planning_paths;
function remember_planning_pathsLoopBegin(remember_planning_pathsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    remember_planning_paths = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'forgetting1.xlsx',
      seed: undefined, name: 'remember_planning_paths'
    });
    psychoJS.experiment.addLoop(remember_planning_paths); // add the loop to the experiment
    currentLoop = remember_planning_paths;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    remember_planning_paths.forEach(function() {
      snapshot = remember_planning_paths.getSnapshot();
    
      remember_planning_pathsLoopScheduler.add(importConditions(snapshot));
      remember_planning_pathsLoopScheduler.add(forgetting_paths1RoutineBegin(snapshot));
      remember_planning_pathsLoopScheduler.add(forgetting_paths1RoutineEachFrame());
      remember_planning_pathsLoopScheduler.add(forgetting_paths1RoutineEnd(snapshot));
      remember_planning_pathsLoopScheduler.add(planningpathstraining2RoutineBegin(snapshot));
      remember_planning_pathsLoopScheduler.add(planningpathstraining2RoutineEachFrame());
      remember_planning_pathsLoopScheduler.add(planningpathstraining2RoutineEnd(snapshot));
      remember_planning_pathsLoopScheduler.add(correct_forget_pathsRoutineBegin(snapshot));
      remember_planning_pathsLoopScheduler.add(correct_forget_pathsRoutineEachFrame());
      remember_planning_pathsLoopScheduler.add(correct_forget_pathsRoutineEnd(snapshot));
      remember_planning_pathsLoopScheduler.add(remember_planning_pathsLoopEndIteration(remember_planning_pathsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function remember_planning_pathsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(remember_planning_paths);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function remember_planning_pathsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _end_instructions_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    end_instructions.keys = undefined;
    end_instructions.rt = undefined;
    _end_instructions_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instruction_test);
    instructionsComponents.push(end_instructions);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_test* updates
    if (t >= 0.0 && instruction_test.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_test.tStart = t;  // (not accounting for frame time here)
      instruction_test.frameNStart = frameN;  // exact frame index
      
      instruction_test.setAutoDraw(true);
    }
    
    
    // *end_instructions* updates
    if (t >= 0.0 && end_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_instructions.tStart = t;  // (not accounting for frame time here)
      end_instructions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_instructions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_instructions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_instructions.clearEvents(); });
    }
    
    if (end_instructions.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_instructions.getKeys({keyList: ['space'], waitRelease: false});
      _end_instructions_allKeys = _end_instructions_allKeys.concat(theseKeys);
      if (_end_instructions_allKeys.length > 0) {
        end_instructions.keys = _end_instructions_allKeys[_end_instructions_allKeys.length - 1].name;  // just the last key pressed
        end_instructions.rt = _end_instructions_allKeys[_end_instructions_allKeys.length - 1].rt;
        end_instructions.duration = _end_instructions_allKeys[_end_instructions_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    end_instructions.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var second_instructionsComponents;
function second_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'second_instructions' ---
    t = 0;
    second_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('second_instructions.started', globalClock.getTime());
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    second_instructionsComponents = [];
    second_instructionsComponents.push(key_resp_2);
    second_instructionsComponents.push(text_22);
    
    second_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function second_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'second_instructions' ---
    // get current time
    t = second_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_22* updates
    if (t >= 0.0 && text_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_22.tStart = t;  // (not accounting for frame time here)
      text_22.frameNStart = frameN;  // exact frame index
      
      text_22.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    second_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function second_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'second_instructions' ---
    second_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('second_instructions.stopped', globalClock.getTime());
    key_resp_2.stop();
    // the Routine "second_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _responseleft_allKeys;
var third_instructionsComponents;
function third_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'third_instructions' ---
    t = 0;
    third_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('third_instructions.started', globalClock.getTime());
    responseleft.keys = undefined;
    responseleft.rt = undefined;
    _responseleft_allKeys = [];
    // keep track of which components have finished
    third_instructionsComponents = [];
    third_instructionsComponents.push(responseleft);
    third_instructionsComponents.push(text_23);
    
    third_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function third_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'third_instructions' ---
    // get current time
    t = third_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *responseleft* updates
    if (t >= 0.2 && responseleft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responseleft.tStart = t;  // (not accounting for frame time here)
      responseleft.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { responseleft.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { responseleft.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { responseleft.clearEvents(); });
    }
    
    if (responseleft.status === PsychoJS.Status.STARTED) {
      let theseKeys = responseleft.getKeys({keyList: ['space'], waitRelease: false});
      _responseleft_allKeys = _responseleft_allKeys.concat(theseKeys);
      if (_responseleft_allKeys.length > 0) {
        responseleft.keys = _responseleft_allKeys[_responseleft_allKeys.length - 1].name;  // just the last key pressed
        responseleft.rt = _responseleft_allKeys[_responseleft_allKeys.length - 1].rt;
        responseleft.duration = _responseleft_allKeys[_responseleft_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_23* updates
    if (t >= 0.0 && text_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_23.tStart = t;  // (not accounting for frame time here)
      text_23.frameNStart = frameN;  // exact frame index
      
      text_23.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    third_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function third_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'third_instructions' ---
    third_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('third_instructions.stopped', globalClock.getTime());
    responseleft.stop();
    // the Routine "third_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructions4Components;
function instructions4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions4' ---
    t = 0;
    instructions4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions4.started', globalClock.getTime());
    // keep track of which components have finished
    instructions4Components = [];
    instructions4Components.push(text_153);
    
    instructions4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions4' ---
    // get current time
    t = instructions4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_153* updates
    if (t >= 0.0 && text_153.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_153.tStart = t;  // (not accounting for frame time here)
      text_153.frameNStart = frameN;  // exact frame index
      
      text_153.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_153.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_153.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions4' ---
    instructions4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions4.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_10_allKeys;
var practice1Components;
function practice1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice1' ---
    t = 0;
    practice1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice1.started', globalClock.getTime());
    image_22.setImage('apple.png');
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    // keep track of which components have finished
    practice1Components = [];
    practice1Components.push(image_22);
    practice1Components.push(key_resp_10);
    practice1Components.push(text_40);
    
    practice1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice1' ---
    // get current time
    t = practice1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_22* updates
    if (t >= 0.0 && image_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_22.tStart = t;  // (not accounting for frame time here)
      image_22.frameNStart = frameN;  // exact frame index
      
      image_22.setAutoDraw(true);
    }
    
    
    // *key_resp_10* updates
    if (t >= 0.2 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }
    
    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: [1, '1', 'left'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        key_resp_10.duration = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_40* updates
    if (t >= 0.0 && text_40.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_40.tStart = t;  // (not accounting for frame time here)
      text_40.frameNStart = frameN;  // exact frame index
      
      text_40.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice1' ---
    practice1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_10.corr, level);
    }
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        psychoJS.experiment.addData('key_resp_10.duration', key_resp_10.duration);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice1_resultComponents;
function practice1_resultRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice1_result' ---
    t = 0;
    practice1_resultClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice1_result.started', globalClock.getTime());
    image_20.setImage(image_prac2);
    // keep track of which components have finished
    practice1_resultComponents = [];
    practice1_resultComponents.push(image_20);
    
    practice1_resultComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice1_resultRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice1_result' ---
    // get current time
    t = practice1_resultClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_20* updates
    if (t >= 0.0 && image_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_20.tStart = t;  // (not accounting for frame time here)
      image_20.frameNStart = frameN;  // exact frame index
      
      image_20.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_20.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_20.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice1_resultComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice1_resultRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice1_result' ---
    practice1_resultComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice1_result.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var next_trialComponents;
function next_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'next_trial' ---
    t = 0;
    next_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('next_trial.started', globalClock.getTime());
    // keep track of which components have finished
    next_trialComponents = [];
    next_trialComponents.push(next_trial_text);
    
    next_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function next_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'next_trial' ---
    // get current time
    t = next_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *next_trial_text* updates
    if (t >= 0.0 && next_trial_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_trial_text.tStart = t;  // (not accounting for frame time here)
      next_trial_text.frameNStart = frameN;  // exact frame index
      
      next_trial_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (next_trial_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      next_trial_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    next_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function next_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'next_trial' ---
    next_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('next_trial.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _practice_answer_allKeys;
var practice1_quizComponents;
function practice1_quizRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice1_quiz' ---
    t = 0;
    practice1_quizClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice1_quiz.started', globalClock.getTime());
    tree_2.setImage('tree.png');
    practice_answer.keys = undefined;
    practice_answer.rt = undefined;
    _practice_answer_allKeys = [];
    // keep track of which components have finished
    practice1_quizComponents = [];
    practice1_quizComponents.push(basket_2);
    practice1_quizComponents.push(fireworks_2);
    practice1_quizComponents.push(tree_2);
    practice1_quizComponents.push(text_24);
    practice1_quizComponents.push(text_25);
    practice1_quizComponents.push(text_27);
    practice1_quizComponents.push(practice_answer);
    practice1_quizComponents.push(text_26);
    
    practice1_quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice1_quizRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice1_quiz' ---
    // get current time
    t = practice1_quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *basket_2* updates
    if (t >= 0.0 && basket_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basket_2.tStart = t;  // (not accounting for frame time here)
      basket_2.frameNStart = frameN;  // exact frame index
      
      basket_2.setAutoDraw(true);
    }
    
    
    // *fireworks_2* updates
    if (t >= 0.0 && fireworks_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fireworks_2.tStart = t;  // (not accounting for frame time here)
      fireworks_2.frameNStart = frameN;  // exact frame index
      
      fireworks_2.setAutoDraw(true);
    }
    
    
    // *tree_2* updates
    if (t >= 0.0 && tree_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tree_2.tStart = t;  // (not accounting for frame time here)
      tree_2.frameNStart = frameN;  // exact frame index
      
      tree_2.setAutoDraw(true);
    }
    
    
    // *text_24* updates
    if (t >= 0.0 && text_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_24.tStart = t;  // (not accounting for frame time here)
      text_24.frameNStart = frameN;  // exact frame index
      
      text_24.setAutoDraw(true);
    }
    
    
    // *text_25* updates
    if (t >= 0.0 && text_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_25.tStart = t;  // (not accounting for frame time here)
      text_25.frameNStart = frameN;  // exact frame index
      
      text_25.setAutoDraw(true);
    }
    
    
    // *text_27* updates
    if (t >= 0.0 && text_27.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_27.tStart = t;  // (not accounting for frame time here)
      text_27.frameNStart = frameN;  // exact frame index
      
      text_27.setAutoDraw(true);
    }
    
    
    // *practice_answer* updates
    if (t >= 0.0 && practice_answer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_answer.tStart = t;  // (not accounting for frame time here)
      practice_answer.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_answer.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_answer.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_answer.clearEvents(); });
    }
    
    if (practice_answer.status === PsychoJS.Status.STARTED) {
      let theseKeys = practice_answer.getKeys({keyList: ['a', 'g', 'l'], waitRelease: false});
      _practice_answer_allKeys = _practice_answer_allKeys.concat(theseKeys);
      if (_practice_answer_allKeys.length > 0) {
        practice_answer.keys = _practice_answer_allKeys[_practice_answer_allKeys.length - 1].name;  // just the last key pressed
        practice_answer.rt = _practice_answer_allKeys[_practice_answer_allKeys.length - 1].rt;
        practice_answer.duration = _practice_answer_allKeys[_practice_answer_allKeys.length - 1].duration;
        // was this correct?
        if (practice_answer.keys == 'a') {
            practice_answer.corr = 1;
        } else {
            practice_answer.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_26* updates
    if (t >= 0.0 && text_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_26.tStart = t;  // (not accounting for frame time here)
      text_26.frameNStart = frameN;  // exact frame index
      
      text_26.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice1_quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice1_quizRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice1_quiz' ---
    practice1_quizComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice1_quiz.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (practice_answer.keys === undefined) {
      if (['None','none',undefined].includes('a')) {
         practice_answer.corr = 1;  // correct non-response
      } else {
         practice_answer.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practice_answer.corr, level);
    }
    psychoJS.experiment.addData('practice_answer.keys', practice_answer.keys);
    psychoJS.experiment.addData('practice_answer.corr', practice_answer.corr);
    if (typeof practice_answer.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_answer.rt', practice_answer.rt);
        psychoJS.experiment.addData('practice_answer.duration', practice_answer.duration);
        routineTimer.reset();
        }
    
    practice_answer.stop();
    // Run 'End Routine' code from code_21
    if (practice_answer.corr) {
        console.log("correct answer");
        practice_loop.finished = true;
    }
    
    // the Routine "practice1_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg;
var practice1_quizfeedbackComponents;
function practice1_quizfeedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice1_quizfeedback' ---
    t = 0;
    practice1_quizfeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice1_quizfeedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_14
    if (practice_answer.corr) {
        msg = "Correct!";
    } else {
        msg = "Wrong! Re-starting practice";
    }
    
    text_30.setText(msg);
    // keep track of which components have finished
    practice1_quizfeedbackComponents = [];
    practice1_quizfeedbackComponents.push(text_30);
    
    practice1_quizfeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice1_quizfeedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice1_quizfeedback' ---
    // get current time
    t = practice1_quizfeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_30* updates
    if (t >= 0.0 && text_30.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_30.tStart = t;  // (not accounting for frame time here)
      text_30.frameNStart = frameN;  // exact frame index
      
      text_30.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_30.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_30.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice1_quizfeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice1_quizfeedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice1_quizfeedback' ---
    practice1_quizfeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice1_quizfeedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_23_allKeys;
var memory_quiz_instructionsComponents;
function memory_quiz_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'memory_quiz_instructions' ---
    t = 0;
    memory_quiz_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('memory_quiz_instructions.started', globalClock.getTime());
    key_resp_23.keys = undefined;
    key_resp_23.rt = undefined;
    _key_resp_23_allKeys = [];
    // keep track of which components have finished
    memory_quiz_instructionsComponents = [];
    memory_quiz_instructionsComponents.push(text_75);
    memory_quiz_instructionsComponents.push(key_resp_23);
    
    memory_quiz_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function memory_quiz_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'memory_quiz_instructions' ---
    // get current time
    t = memory_quiz_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_75* updates
    if (t >= 0.0 && text_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_75.tStart = t;  // (not accounting for frame time here)
      text_75.frameNStart = frameN;  // exact frame index
      
      text_75.setAutoDraw(true);
    }
    
    
    // *key_resp_23* updates
    if (t >= 0.0 && key_resp_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_23.tStart = t;  // (not accounting for frame time here)
      key_resp_23.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_23.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_23.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_23.clearEvents(); });
    }
    
    if (key_resp_23.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_23.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_23_allKeys = _key_resp_23_allKeys.concat(theseKeys);
      if (_key_resp_23_allKeys.length > 0) {
        key_resp_23.keys = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].name;  // just the last key pressed
        key_resp_23.rt = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].rt;
        key_resp_23.duration = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    memory_quiz_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memory_quiz_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'memory_quiz_instructions' ---
    memory_quiz_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('memory_quiz_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_23.corr, level);
    }
    psychoJS.experiment.addData('key_resp_23.keys', key_resp_23.keys);
    if (typeof key_resp_23.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_23.rt', key_resp_23.rt);
        psychoJS.experiment.addData('key_resp_23.duration', key_resp_23.duration);
        routineTimer.reset();
        }
    
    key_resp_23.stop();
    // the Routine "memory_quiz_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_17_allKeys;
var quiz1_iComponents;
function quiz1_iRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz1_i' ---
    t = 0;
    quiz1_iClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz1_i.started', globalClock.getTime());
    key_resp_17.keys = undefined;
    key_resp_17.rt = undefined;
    _key_resp_17_allKeys = [];
    // keep track of which components have finished
    quiz1_iComponents = [];
    quiz1_iComponents.push(text_43);
    quiz1_iComponents.push(key_resp_17);
    
    quiz1_iComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz1_iRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz1_i' ---
    // get current time
    t = quiz1_iClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_43* updates
    if (t >= 0.0 && text_43.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_43.tStart = t;  // (not accounting for frame time here)
      text_43.frameNStart = frameN;  // exact frame index
      
      text_43.setAutoDraw(true);
    }
    
    
    // *key_resp_17* updates
    if (t >= 0.0 && key_resp_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_17.tStart = t;  // (not accounting for frame time here)
      key_resp_17.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_17.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.clearEvents(); });
    }
    
    if (key_resp_17.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_17.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_17_allKeys = _key_resp_17_allKeys.concat(theseKeys);
      if (_key_resp_17_allKeys.length > 0) {
        key_resp_17.keys = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].name;  // just the last key pressed
        key_resp_17.rt = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].rt;
        key_resp_17.duration = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz1_iComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct;
function quiz1_iRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz1_i' ---
    quiz1_iComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz1_i.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_27
    correct = 0;
    if ((key_resp_17.keys === "c")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_17.corr, level);
    }
    psychoJS.experiment.addData('key_resp_17.keys', key_resp_17.keys);
    if (typeof key_resp_17.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_17.rt', key_resp_17.rt);
        psychoJS.experiment.addData('key_resp_17.duration', key_resp_17.duration);
        routineTimer.reset();
        }
    
    key_resp_17.stop();
    // the Routine "quiz1_i" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_18_allKeys;
var quiz2_iComponents;
function quiz2_iRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz2_i' ---
    t = 0;
    quiz2_iClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz2_i.started', globalClock.getTime());
    key_resp_18.keys = undefined;
    key_resp_18.rt = undefined;
    _key_resp_18_allKeys = [];
    // keep track of which components have finished
    quiz2_iComponents = [];
    quiz2_iComponents.push(text_70);
    quiz2_iComponents.push(key_resp_18);
    
    quiz2_iComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz2_iRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz2_i' ---
    // get current time
    t = quiz2_iClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_70* updates
    if (t >= 0.0 && text_70.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_70.tStart = t;  // (not accounting for frame time here)
      text_70.frameNStart = frameN;  // exact frame index
      
      text_70.setAutoDraw(true);
    }
    
    
    // *key_resp_18* updates
    if (t >= 0.0 && key_resp_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_18.tStart = t;  // (not accounting for frame time here)
      key_resp_18.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_18.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.clearEvents(); });
    }
    
    if (key_resp_18.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_18.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_18_allKeys = _key_resp_18_allKeys.concat(theseKeys);
      if (_key_resp_18_allKeys.length > 0) {
        key_resp_18.keys = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].name;  // just the last key pressed
        key_resp_18.rt = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].rt;
        key_resp_18.duration = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz2_iComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz2_iRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz2_i' ---
    quiz2_iComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz2_i.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_30
    if ((key_resp_18.keys === "c")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_18.corr, level);
    }
    psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
    if (typeof key_resp_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
        psychoJS.experiment.addData('key_resp_18.duration', key_resp_18.duration);
        routineTimer.reset();
        }
    
    key_resp_18.stop();
    // the Routine "quiz2_i" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_19_allKeys;
var quiz3Components;
function quiz3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz3' ---
    t = 0;
    quiz3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz3.started', globalClock.getTime());
    key_resp_19.keys = undefined;
    key_resp_19.rt = undefined;
    _key_resp_19_allKeys = [];
    // keep track of which components have finished
    quiz3Components = [];
    quiz3Components.push(text_71);
    quiz3Components.push(key_resp_19);
    
    quiz3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz3' ---
    // get current time
    t = quiz3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_71* updates
    if (t >= 0.0 && text_71.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_71.tStart = t;  // (not accounting for frame time here)
      text_71.frameNStart = frameN;  // exact frame index
      
      text_71.setAutoDraw(true);
    }
    
    
    // *key_resp_19* updates
    if (t >= 0.0 && key_resp_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_19.tStart = t;  // (not accounting for frame time here)
      key_resp_19.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_19.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.clearEvents(); });
    }
    
    if (key_resp_19.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_19.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_19_allKeys = _key_resp_19_allKeys.concat(theseKeys);
      if (_key_resp_19_allKeys.length > 0) {
        key_resp_19.keys = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].name;  // just the last key pressed
        key_resp_19.rt = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].rt;
        key_resp_19.duration = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz3' ---
    quiz3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_31
    if ((key_resp_19.keys === "b")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_19.corr, level);
    }
    psychoJS.experiment.addData('key_resp_19.keys', key_resp_19.keys);
    if (typeof key_resp_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_19.rt', key_resp_19.rt);
        psychoJS.experiment.addData('key_resp_19.duration', key_resp_19.duration);
        routineTimer.reset();
        }
    
    key_resp_19.stop();
    // the Routine "quiz3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_20_allKeys;
var quiz4Components;
function quiz4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz4' ---
    t = 0;
    quiz4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz4.started', globalClock.getTime());
    key_resp_20.keys = undefined;
    key_resp_20.rt = undefined;
    _key_resp_20_allKeys = [];
    // keep track of which components have finished
    quiz4Components = [];
    quiz4Components.push(text_72);
    quiz4Components.push(key_resp_20);
    
    quiz4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz4' ---
    // get current time
    t = quiz4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_72* updates
    if (t >= 0.0 && text_72.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_72.tStart = t;  // (not accounting for frame time here)
      text_72.frameNStart = frameN;  // exact frame index
      
      text_72.setAutoDraw(true);
    }
    
    
    // *key_resp_20* updates
    if (t >= 0.0 && key_resp_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_20.tStart = t;  // (not accounting for frame time here)
      key_resp_20.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_20.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.clearEvents(); });
    }
    
    if (key_resp_20.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_20.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_20_allKeys = _key_resp_20_allKeys.concat(theseKeys);
      if (_key_resp_20_allKeys.length > 0) {
        key_resp_20.keys = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].name;  // just the last key pressed
        key_resp_20.rt = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].rt;
        key_resp_20.duration = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz4' ---
    quiz4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz4.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_35
    if ((key_resp_20.keys === "b")) {
        correct += 1;
    }
    if ((correct === 4)) {
        instructions_get_right.finished = true;
        msg = "Correct! You can now move on";
    } else {
        msg = "Incorrect! You need to repeat the instructions.";
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_20.corr, level);
    }
    psychoJS.experiment.addData('key_resp_20.keys', key_resp_20.keys);
    if (typeof key_resp_20.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_20.rt', key_resp_20.rt);
        psychoJS.experiment.addData('key_resp_20.duration', key_resp_20.duration);
        routineTimer.reset();
        }
    
    key_resp_20.stop();
    // the Routine "quiz4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quiz_feedbackComponents;
function quiz_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz_feedback' ---
    t = 0;
    quiz_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.250000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz_feedback.started', globalClock.getTime());
    result_q_instr.setText(msg);
    // keep track of which components have finished
    quiz_feedbackComponents = [];
    quiz_feedbackComponents.push(result_q_instr);
    
    quiz_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz_feedback' ---
    // get current time
    t = quiz_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *result_q_instr* updates
    if (t >= 0.0 && result_q_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      result_q_instr.tStart = t;  // (not accounting for frame time here)
      result_q_instr.frameNStart = frameN;  // exact frame index
      
      result_q_instr.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (result_q_instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      result_q_instr.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz_feedback' ---
    quiz_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz_feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_7_allKeys;
var start_learningComponents;
function start_learningRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_learning' ---
    t = 0;
    start_learningClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('start_learning.started', globalClock.getTime());
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    start_learningComponents = [];
    start_learningComponents.push(text_31);
    start_learningComponents.push(key_resp_7);
    
    start_learningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function start_learningRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_learning' ---
    // get current time
    t = start_learningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_31* updates
    if (t >= 0.0 && text_31.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_31.tStart = t;  // (not accounting for frame time here)
      text_31.frameNStart = frameN;  // exact frame index
      
      text_31.setAutoDraw(true);
    }
    
    
    // *key_resp_7* updates
    if (t >= 0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }
    
    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        key_resp_7.duration = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    start_learningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_learningRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_learning' ---
    start_learningComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('start_learning.stopped', globalClock.getTime());
    key_resp_7.stop();
    // the Routine "start_learning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var learn1Components;
function learn1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'learn1' ---
    t = 0;
    learn1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('learn1.started', globalClock.getTime());
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    image_1.setImage(image1);
    text.setText(action1);
    // keep track of which components have finished
    learn1Components = [];
    learn1Components.push(key_resp);
    learn1Components.push(image_1);
    learn1Components.push(text);
    
    learn1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function learn1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'learn1' ---
    // get current time
    t = learn1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp.keys == corr_ans) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_1* updates
    if (t >= 0.0 && image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1.tStart = t;  // (not accounting for frame time here)
      image_1.frameNStart = frameN;  // exact frame index
      
      image_1.setAutoDraw(true);
    }
    
    
    // *text* updates
    if (t >= 1 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    learn1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'learn1' ---
    learn1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('learn1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_ans)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "learn1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg_incorrect;
var check_incorrect1Components;
function check_incorrect1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'check_incorrect1' ---
    t = 0;
    check_incorrect1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('check_incorrect1.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_3
    if (key_resp.corr) {
        msg_incorrect = "correct";
        incorrect_loop.finished = true;
        continueRoutine = false;
    } else {
        msg_incorrect = "You clicked the wrong button! If you click the wrong button 5 times, the game will stop and you will NOT GET PAID because you failed to follow instructions!";
        incorrect_actions += 1;
        continueRoutine = true;
        if ((incorrect_actions > 14)) {
            psychoJS.quit();
        }
    }
    
    text_incorrect_2.setText(msg_incorrect);
    // keep track of which components have finished
    check_incorrect1Components = [];
    check_incorrect1Components.push(text_incorrect_2);
    
    check_incorrect1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function check_incorrect1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'check_incorrect1' ---
    // get current time
    t = check_incorrect1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_incorrect_2* updates
    if (t >= 0.0 && text_incorrect_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_incorrect_2.tStart = t;  // (not accounting for frame time here)
      text_incorrect_2.frameNStart = frameN;  // exact frame index
      
      text_incorrect_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_incorrect_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_incorrect_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    check_incorrect1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function check_incorrect1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'check_incorrect1' ---
    check_incorrect1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('check_incorrect1.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var learn2Components;
function learn2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'learn2' ---
    t = 0;
    learn2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('learn2.started', globalClock.getTime());
    image_2.setImage(image2);
    // keep track of which components have finished
    learn2Components = [];
    learn2Components.push(image_2);
    
    learn2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function learn2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'learn2' ---
    // get current time
    t = learn2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    learn2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learn2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'learn2' ---
    learn2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('learn2.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quiz1_score;
var quiz2_score;
var counter_quizzes_roundComponents;
function counter_quizzes_roundRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'counter_quizzes_round' ---
    t = 0;
    counter_quizzes_roundClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('counter_quizzes_round.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_46
    quiz1_score = 0;
    quiz2_score = 0;
    
    // keep track of which components have finished
    counter_quizzes_roundComponents = [];
    
    counter_quizzes_roundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function counter_quizzes_roundRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'counter_quizzes_round' ---
    // get current time
    t = counter_quizzes_roundClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    counter_quizzes_roundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function counter_quizzes_roundRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'counter_quizzes_round' ---
    counter_quizzes_roundComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('counter_quizzes_round.stopped', globalClock.getTime());
    // the Routine "counter_quizzes_round" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quiz1_count;
var quiz2_count;
var betweenComponents;
function betweenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'between' ---
    t = 0;
    betweenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('between.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_39
    quiz1_count = 1;
    quiz2_count = 1;
    
    // keep track of which components have finished
    betweenComponents = [];
    betweenComponents.push(text_2);
    
    betweenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function betweenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'between' ---
    // get current time
    t = betweenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    betweenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function betweenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'between' ---
    betweenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('between.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _answer_quiz1_allKeys;
var quizComponents;
function quizRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz' ---
    t = 0;
    quizClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz.started', globalClock.getTime());
    target_quiz1.setImage(image1);
    question_quiz1.setText(question);
    answer_quiz1.keys = undefined;
    answer_quiz1.rt = undefined;
    _answer_quiz1_allKeys = [];
    answer1.setImage(ans1);
    answer2.setImage(ans2);
    answer3.setImage(ans3);
    answer4.setImage(ans4);
    // keep track of which components have finished
    quizComponents = [];
    quizComponents.push(target_quiz1);
    quizComponents.push(question_quiz1);
    quizComponents.push(answer_quiz1);
    quizComponents.push(answer1);
    quizComponents.push(answer2);
    quizComponents.push(answer3);
    quizComponents.push(answer4);
    quizComponents.push(a1);
    quizComponents.push(a2);
    quizComponents.push(a3);
    quizComponents.push(a4);
    
    quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quizRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz' ---
    // get current time
    t = quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_quiz1* updates
    if (t >= 0.0 && target_quiz1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_quiz1.tStart = t;  // (not accounting for frame time here)
      target_quiz1.frameNStart = frameN;  // exact frame index
      
      target_quiz1.setAutoDraw(true);
    }
    
    
    // *question_quiz1* updates
    if (t >= 0.0 && question_quiz1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_quiz1.tStart = t;  // (not accounting for frame time here)
      question_quiz1.frameNStart = frameN;  // exact frame index
      
      question_quiz1.setAutoDraw(true);
    }
    
    
    // *answer_quiz1* updates
    if (t >= 0.0 && answer_quiz1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer_quiz1.tStart = t;  // (not accounting for frame time here)
      answer_quiz1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { answer_quiz1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1.clearEvents(); });
    }
    
    if (answer_quiz1.status === PsychoJS.Status.STARTED) {
      let theseKeys = answer_quiz1.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _answer_quiz1_allKeys = _answer_quiz1_allKeys.concat(theseKeys);
      if (_answer_quiz1_allKeys.length > 0) {
        answer_quiz1.keys = _answer_quiz1_allKeys[_answer_quiz1_allKeys.length - 1].name;  // just the last key pressed
        answer_quiz1.rt = _answer_quiz1_allKeys[_answer_quiz1_allKeys.length - 1].rt;
        answer_quiz1.duration = _answer_quiz1_allKeys[_answer_quiz1_allKeys.length - 1].duration;
        // was this correct?
        if (answer_quiz1.keys == corr_ans) {
            answer_quiz1.corr = 1;
        } else {
            answer_quiz1.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *answer1* updates
    if (t >= 0.0 && answer1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer1.tStart = t;  // (not accounting for frame time here)
      answer1.frameNStart = frameN;  // exact frame index
      
      answer1.setAutoDraw(true);
    }
    
    
    // *answer2* updates
    if (t >= 0.0 && answer2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer2.tStart = t;  // (not accounting for frame time here)
      answer2.frameNStart = frameN;  // exact frame index
      
      answer2.setAutoDraw(true);
    }
    
    
    // *answer3* updates
    if (t >= 0.0 && answer3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer3.tStart = t;  // (not accounting for frame time here)
      answer3.frameNStart = frameN;  // exact frame index
      
      answer3.setAutoDraw(true);
    }
    
    
    // *answer4* updates
    if (t >= 0.0 && answer4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer4.tStart = t;  // (not accounting for frame time here)
      answer4.frameNStart = frameN;  // exact frame index
      
      answer4.setAutoDraw(true);
    }
    
    
    // *a1* updates
    if (t >= 0.0 && a1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a1.tStart = t;  // (not accounting for frame time here)
      a1.frameNStart = frameN;  // exact frame index
      
      a1.setAutoDraw(true);
    }
    
    
    // *a2* updates
    if (t >= 0.0 && a2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a2.tStart = t;  // (not accounting for frame time here)
      a2.frameNStart = frameN;  // exact frame index
      
      a2.setAutoDraw(true);
    }
    
    
    // *a3* updates
    if (t >= 0.0 && a3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a3.tStart = t;  // (not accounting for frame time here)
      a3.frameNStart = frameN;  // exact frame index
      
      a3.setAutoDraw(true);
    }
    
    
    // *a4* updates
    if (t >= 0.0 && a4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a4.tStart = t;  // (not accounting for frame time here)
      a4.frameNStart = frameN;  // exact frame index
      
      a4.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quizRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz' ---
    quizComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (answer_quiz1.keys === undefined) {
      if (['None','none',undefined].includes(corr_ans)) {
         answer_quiz1.corr = 1;  // correct non-response
      } else {
         answer_quiz1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(answer_quiz1.corr, level);
    }
    psychoJS.experiment.addData('answer_quiz1.keys', answer_quiz1.keys);
    psychoJS.experiment.addData('answer_quiz1.corr', answer_quiz1.corr);
    if (typeof answer_quiz1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('answer_quiz1.rt', answer_quiz1.rt);
        psychoJS.experiment.addData('answer_quiz1.duration', answer_quiz1.duration);
        routineTimer.reset();
        }
    
    answer_quiz1.stop();
    // Run 'End Routine' code from code_38
    if (answer_quiz1.corr) {
        quiz1_score += 1;
        msg = "Correct! Good job!";
    } else {
        msg = "INCORRECT :(";
    }
    
    // the Routine "quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var back_to_learnComponents;
function back_to_learnRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'back_to_learn' ---
    t = 0;
    back_to_learnClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('back_to_learn.started', globalClock.getTime());
    // keep track of which components have finished
    back_to_learnComponents = [];
    back_to_learnComponents.push(text_8);
    
    back_to_learnComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function back_to_learnRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'back_to_learn' ---
    // get current time
    t = back_to_learnClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }
    
    frameRemains = 0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_8.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    back_to_learnComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function back_to_learnRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'back_to_learn' ---
    back_to_learnComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('back_to_learn.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var check_incorrectComponents;
function check_incorrectRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'check_incorrect' ---
    t = 0;
    check_incorrectClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('check_incorrect.started', globalClock.getTime());
    // Run 'Begin Routine' code from code
    if (key_resp.corr) {
        msg_incorrect = "correct";
        incorrect_loop2.finished = true;
        continueRoutine = false;
    } else {
        msg_incorrect = "You clicked the wrong button! If you click the wrong button 5 times, the game will stop and you will NOT GET PAID because you failed to follow instructions!";
        incorrect_actions += 1;
        continueRoutine = true;
        if ((incorrect_actions > 15)) {
            psychoJS.quit();
        }
    }
    
    text_incorrect.setText(msg_incorrect);
    // keep track of which components have finished
    check_incorrectComponents = [];
    check_incorrectComponents.push(text_incorrect);
    
    check_incorrectComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function check_incorrectRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'check_incorrect' ---
    // get current time
    t = check_incorrectClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_incorrect* updates
    if (t >= 0.0 && text_incorrect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_incorrect.tStart = t;  // (not accounting for frame time here)
      text_incorrect.frameNStart = frameN;  // exact frame index
      
      text_incorrect.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_incorrect.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_incorrect.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    check_incorrectComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function check_incorrectRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'check_incorrect' ---
    check_incorrectComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('check_incorrect.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _answer_quiz1_2_allKeys;
var quiz2Components;
function quiz2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz2' ---
    t = 0;
    quiz2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz2.started', globalClock.getTime());
    target_quiz1_2.setImage(image1);
    question_quiz1_2.setText(question);
    answer_quiz1_2.keys = undefined;
    answer_quiz1_2.rt = undefined;
    _answer_quiz1_2_allKeys = [];
    answer1_2.setImage(ans1);
    answer2_2.setImage(ans2);
    answer3_2.setImage(ans3);
    answer4_2.setImage(ans4);
    // keep track of which components have finished
    quiz2Components = [];
    quiz2Components.push(target_quiz1_2);
    quiz2Components.push(question_quiz1_2);
    quiz2Components.push(answer_quiz1_2);
    quiz2Components.push(answer1_2);
    quiz2Components.push(answer2_2);
    quiz2Components.push(answer3_2);
    quiz2Components.push(answer4_2);
    quiz2Components.push(a1_2);
    quiz2Components.push(a2_2);
    quiz2Components.push(a3_2);
    quiz2Components.push(a4_2);
    
    quiz2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz2' ---
    // get current time
    t = quiz2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target_quiz1_2* updates
    if (t >= 0.0 && target_quiz1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_quiz1_2.tStart = t;  // (not accounting for frame time here)
      target_quiz1_2.frameNStart = frameN;  // exact frame index
      
      target_quiz1_2.setAutoDraw(true);
    }
    
    
    // *question_quiz1_2* updates
    if (t >= 0.0 && question_quiz1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_quiz1_2.tStart = t;  // (not accounting for frame time here)
      question_quiz1_2.frameNStart = frameN;  // exact frame index
      
      question_quiz1_2.setAutoDraw(true);
    }
    
    
    // *answer_quiz1_2* updates
    if (t >= 0.0 && answer_quiz1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer_quiz1_2.tStart = t;  // (not accounting for frame time here)
      answer_quiz1_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { answer_quiz1_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1_2.clearEvents(); });
    }
    
    if (answer_quiz1_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = answer_quiz1_2.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _answer_quiz1_2_allKeys = _answer_quiz1_2_allKeys.concat(theseKeys);
      if (_answer_quiz1_2_allKeys.length > 0) {
        answer_quiz1_2.keys = _answer_quiz1_2_allKeys[_answer_quiz1_2_allKeys.length - 1].name;  // just the last key pressed
        answer_quiz1_2.rt = _answer_quiz1_2_allKeys[_answer_quiz1_2_allKeys.length - 1].rt;
        answer_quiz1_2.duration = _answer_quiz1_2_allKeys[_answer_quiz1_2_allKeys.length - 1].duration;
        // was this correct?
        if (answer_quiz1_2.keys == corr_ans) {
            answer_quiz1_2.corr = 1;
        } else {
            answer_quiz1_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *answer1_2* updates
    if (t >= 0.0 && answer1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer1_2.tStart = t;  // (not accounting for frame time here)
      answer1_2.frameNStart = frameN;  // exact frame index
      
      answer1_2.setAutoDraw(true);
    }
    
    
    // *answer2_2* updates
    if (t >= 0.0 && answer2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer2_2.tStart = t;  // (not accounting for frame time here)
      answer2_2.frameNStart = frameN;  // exact frame index
      
      answer2_2.setAutoDraw(true);
    }
    
    
    // *answer3_2* updates
    if (t >= 0.0 && answer3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer3_2.tStart = t;  // (not accounting for frame time here)
      answer3_2.frameNStart = frameN;  // exact frame index
      
      answer3_2.setAutoDraw(true);
    }
    
    
    // *answer4_2* updates
    if (t >= 0.0 && answer4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer4_2.tStart = t;  // (not accounting for frame time here)
      answer4_2.frameNStart = frameN;  // exact frame index
      
      answer4_2.setAutoDraw(true);
    }
    
    
    // *a1_2* updates
    if (t >= 0.0 && a1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a1_2.tStart = t;  // (not accounting for frame time here)
      a1_2.frameNStart = frameN;  // exact frame index
      
      a1_2.setAutoDraw(true);
    }
    
    
    // *a2_2* updates
    if (t >= 0.0 && a2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a2_2.tStart = t;  // (not accounting for frame time here)
      a2_2.frameNStart = frameN;  // exact frame index
      
      a2_2.setAutoDraw(true);
    }
    
    
    // *a3_2* updates
    if (t >= 0.0 && a3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a3_2.tStart = t;  // (not accounting for frame time here)
      a3_2.frameNStart = frameN;  // exact frame index
      
      a3_2.setAutoDraw(true);
    }
    
    
    // *a4_2* updates
    if (t >= 0.0 && a4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a4_2.tStart = t;  // (not accounting for frame time here)
      a4_2.frameNStart = frameN;  // exact frame index
      
      a4_2.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz2' ---
    quiz2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (answer_quiz1_2.keys === undefined) {
      if (['None','none',undefined].includes(corr_ans)) {
         answer_quiz1_2.corr = 1;  // correct non-response
      } else {
         answer_quiz1_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(answer_quiz1_2.corr, level);
    }
    psychoJS.experiment.addData('answer_quiz1_2.keys', answer_quiz1_2.keys);
    psychoJS.experiment.addData('answer_quiz1_2.corr', answer_quiz1_2.corr);
    if (typeof answer_quiz1_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('answer_quiz1_2.rt', answer_quiz1_2.rt);
        psychoJS.experiment.addData('answer_quiz1_2.duration', answer_quiz1_2.duration);
        routineTimer.reset();
        }
    
    answer_quiz1_2.stop();
    // Run 'End Routine' code from code_45
    if (answer_quiz1_2.corr) {
        quiz2_score += 1;
        msg = "Correct! Good job!";
    } else {
        msg = "INCORRECT :(";
    }
    
    // the Routine "quiz2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quiz_planning_corr;
var _key_resp_40_allKeys;
var planning_pathsComponents;
function planning_pathsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'planning_paths' ---
    t = 0;
    planning_pathsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('planning_paths.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_42
    quiz1_count = 1;
    quiz_planning_corr = 0;
    
    key_resp_40.keys = undefined;
    key_resp_40.rt = undefined;
    _key_resp_40_allKeys = [];
    // keep track of which components have finished
    planning_pathsComponents = [];
    planning_pathsComponents.push(text_149);
    planning_pathsComponents.push(key_resp_40);
    planning_pathsComponents.push(text_49);
    
    planning_pathsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function planning_pathsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'planning_paths' ---
    // get current time
    t = planning_pathsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_149* updates
    if (t >= 0 && text_149.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_149.tStart = t;  // (not accounting for frame time here)
      text_149.frameNStart = frameN;  // exact frame index
      
      text_149.setAutoDraw(true);
    }
    
    
    // *key_resp_40* updates
    if (t >= 5.0 && key_resp_40.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_40.tStart = t;  // (not accounting for frame time here)
      key_resp_40.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_40.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_40.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_40.clearEvents(); });
    }
    
    if (key_resp_40.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_40.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_40_allKeys = _key_resp_40_allKeys.concat(theseKeys);
      if (_key_resp_40_allKeys.length > 0) {
        key_resp_40.keys = _key_resp_40_allKeys[_key_resp_40_allKeys.length - 1].name;  // just the last key pressed
        key_resp_40.rt = _key_resp_40_allKeys[_key_resp_40_allKeys.length - 1].rt;
        key_resp_40.duration = _key_resp_40_allKeys[_key_resp_40_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_49* updates
    if (t >= 5.0 && text_49.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_49.tStart = t;  // (not accounting for frame time here)
      text_49.frameNStart = frameN;  // exact frame index
      
      text_49.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    planning_pathsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function planning_pathsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'planning_paths' ---
    planning_pathsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('planning_paths.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_40.corr, level);
    }
    psychoJS.experiment.addData('key_resp_40.keys', key_resp_40.keys);
    if (typeof key_resp_40.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_40.rt', key_resp_40.rt);
        psychoJS.experiment.addData('key_resp_40.duration', key_resp_40.duration);
        routineTimer.reset();
        }
    
    key_resp_40.stop();
    // the Routine "planning_paths" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _answer_quiz1_3_allKeys;
var forgetting_paths1Components;
function forgetting_paths1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'forgetting_paths1' ---
    t = 0;
    forgetting_paths1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(120.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('forgetting_paths1.started', globalClock.getTime());
    answer_quiz1_3.keys = undefined;
    answer_quiz1_3.rt = undefined;
    _answer_quiz1_3_allKeys = [];
    answer1_3.setImage(ans1);
    answer2_3.setImage(ans2);
    answer3_3.setImage(ans3);
    // keep track of which components have finished
    forgetting_paths1Components = [];
    forgetting_paths1Components.push(question_quiz1_3);
    forgetting_paths1Components.push(answer_quiz1_3);
    forgetting_paths1Components.push(answer1_3);
    forgetting_paths1Components.push(answer2_3);
    forgetting_paths1Components.push(answer3_3);
    forgetting_paths1Components.push(a1_3);
    forgetting_paths1Components.push(a2_3);
    forgetting_paths1Components.push(text_146);
    
    forgetting_paths1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function forgetting_paths1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'forgetting_paths1' ---
    // get current time
    t = forgetting_paths1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_quiz1_3* updates
    if (t >= 0.0 && question_quiz1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_quiz1_3.tStart = t;  // (not accounting for frame time here)
      question_quiz1_3.frameNStart = frameN;  // exact frame index
      
      question_quiz1_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (question_quiz1_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      question_quiz1_3.setAutoDraw(false);
    }
    
    // *answer_quiz1_3* updates
    if (t >= 0 && answer_quiz1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer_quiz1_3.tStart = t;  // (not accounting for frame time here)
      answer_quiz1_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { answer_quiz1_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1_3.clearEvents(); });
    }
    
    frameRemains = 0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer_quiz1_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer_quiz1_3.status = PsychoJS.Status.FINISHED;
        }
      
    if (answer_quiz1_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = answer_quiz1_3.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _answer_quiz1_3_allKeys = _answer_quiz1_3_allKeys.concat(theseKeys);
      if (_answer_quiz1_3_allKeys.length > 0) {
        answer_quiz1_3.keys = _answer_quiz1_3_allKeys[0].name;  // just the first key pressed
        answer_quiz1_3.rt = _answer_quiz1_3_allKeys[0].rt;
        answer_quiz1_3.duration = _answer_quiz1_3_allKeys[0].duration;
        // was this correct?
        if (answer_quiz1_3.keys == correct_answer1) {
            answer_quiz1_3.corr = 1;
        } else {
            answer_quiz1_3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *answer1_3* updates
    if (t >= 0.0 && answer1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer1_3.tStart = t;  // (not accounting for frame time here)
      answer1_3.frameNStart = frameN;  // exact frame index
      
      answer1_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer1_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer1_3.setAutoDraw(false);
    }
    
    // *answer2_3* updates
    if (t >= 0.0 && answer2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer2_3.tStart = t;  // (not accounting for frame time here)
      answer2_3.frameNStart = frameN;  // exact frame index
      
      answer2_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer2_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer2_3.setAutoDraw(false);
    }
    
    // *answer3_3* updates
    if (t >= 0.0 && answer3_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer3_3.tStart = t;  // (not accounting for frame time here)
      answer3_3.frameNStart = frameN;  // exact frame index
      
      answer3_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer3_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer3_3.setAutoDraw(false);
    }
    
    // *a1_3* updates
    if (t >= 0.0 && a1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a1_3.tStart = t;  // (not accounting for frame time here)
      a1_3.frameNStart = frameN;  // exact frame index
      
      a1_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (a1_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      a1_3.setAutoDraw(false);
    }
    
    // *a2_3* updates
    if (t >= 0.0 && a2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a2_3.tStart = t;  // (not accounting for frame time here)
      a2_3.frameNStart = frameN;  // exact frame index
      
      a2_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (a2_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      a2_3.setAutoDraw(false);
    }
    
    // *text_146* updates
    if (t >= 0.0 && text_146.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_146.tStart = t;  // (not accounting for frame time here)
      text_146.frameNStart = frameN;  // exact frame index
      
      text_146.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_146.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_146.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    forgetting_paths1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function forgetting_paths1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'forgetting_paths1' ---
    forgetting_paths1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('forgetting_paths1.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (answer_quiz1_3.keys === undefined) {
      if (['None','none',undefined].includes(correct_answer1)) {
         answer_quiz1_3.corr = 1;  // correct non-response
      } else {
         answer_quiz1_3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(answer_quiz1_3.corr, level);
    }
    psychoJS.experiment.addData('answer_quiz1_3.keys', answer_quiz1_3.keys);
    psychoJS.experiment.addData('answer_quiz1_3.corr', answer_quiz1_3.corr);
    if (typeof answer_quiz1_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('answer_quiz1_3.rt', answer_quiz1_3.rt);
        psychoJS.experiment.addData('answer_quiz1_3.duration', answer_quiz1_3.duration);
        routineTimer.reset();
        }
    
    answer_quiz1_3.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _answer_quiz1_5_allKeys;
var thisResp;
var planningpathstraining2Components;
function planningpathstraining2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'planningpathstraining2' ---
    t = 0;
    planningpathstraining2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(120.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('planningpathstraining2.started', globalClock.getTime());
    answer_quiz1_5.keys = undefined;
    answer_quiz1_5.rt = undefined;
    _answer_quiz1_5_allKeys = [];
    answer1_5.setImage(ans1);
    answer2_5.setImage(ans2);
    answer3_5.setImage(ans3);
    thisResp = [];
    
    // keep track of which components have finished
    planningpathstraining2Components = [];
    planningpathstraining2Components.push(question_quiz1_5);
    planningpathstraining2Components.push(answer_quiz1_5);
    planningpathstraining2Components.push(answer1_5);
    planningpathstraining2Components.push(answer2_5);
    planningpathstraining2Components.push(answer3_5);
    planningpathstraining2Components.push(a1_5);
    planningpathstraining2Components.push(a2_5);
    planningpathstraining2Components.push(text_152);
    
    planningpathstraining2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function planningpathstraining2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'planningpathstraining2' ---
    // get current time
    t = planningpathstraining2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *question_quiz1_5* updates
    if (t >= 0.0 && question_quiz1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_quiz1_5.tStart = t;  // (not accounting for frame time here)
      question_quiz1_5.frameNStart = frameN;  // exact frame index
      
      question_quiz1_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (question_quiz1_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      question_quiz1_5.setAutoDraw(false);
    }
    
    // *answer_quiz1_5* updates
    if (t >= 0 && answer_quiz1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer_quiz1_5.tStart = t;  // (not accounting for frame time here)
      answer_quiz1_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { answer_quiz1_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { answer_quiz1_5.clearEvents(); });
    }
    
    frameRemains = 0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer_quiz1_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer_quiz1_5.status = PsychoJS.Status.FINISHED;
        }
      
    if (answer_quiz1_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = answer_quiz1_5.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _answer_quiz1_5_allKeys = _answer_quiz1_5_allKeys.concat(theseKeys);
      if (_answer_quiz1_5_allKeys.length > 0) {
        answer_quiz1_5.keys = _answer_quiz1_5_allKeys[0].name;  // just the first key pressed
        answer_quiz1_5.rt = _answer_quiz1_5_allKeys[0].rt;
        answer_quiz1_5.duration = _answer_quiz1_5_allKeys[0].duration;
        // was this correct?
        if (answer_quiz1_5.keys == correct_answer2) {
            answer_quiz1_5.corr = 1;
        } else {
            answer_quiz1_5.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *answer1_5* updates
    if (t >= 0.0 && answer1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer1_5.tStart = t;  // (not accounting for frame time here)
      answer1_5.frameNStart = frameN;  // exact frame index
      
      answer1_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer1_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer1_5.setAutoDraw(false);
    }
    
    // *answer2_5* updates
    if (t >= 0.0 && answer2_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer2_5.tStart = t;  // (not accounting for frame time here)
      answer2_5.frameNStart = frameN;  // exact frame index
      
      answer2_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer2_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer2_5.setAutoDraw(false);
    }
    
    // *answer3_5* updates
    if (t >= 0.0 && answer3_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer3_5.tStart = t;  // (not accounting for frame time here)
      answer3_5.frameNStart = frameN;  // exact frame index
      
      answer3_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (answer3_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      answer3_5.setAutoDraw(false);
    }
    
    // *a1_5* updates
    if (t >= 0.0 && a1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a1_5.tStart = t;  // (not accounting for frame time here)
      a1_5.frameNStart = frameN;  // exact frame index
      
      a1_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (a1_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      a1_5.setAutoDraw(false);
    }
    
    // *a2_5* updates
    if (t >= 0.0 && a2_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      a2_5.tStart = t;  // (not accounting for frame time here)
      a2_5.frameNStart = frameN;  // exact frame index
      
      a2_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (a2_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      a2_5.setAutoDraw(false);
    }
    
    // *text_152* updates
    if (t >= 0.0 && text_152.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_152.tStart = t;  // (not accounting for frame time here)
      text_152.frameNStart = frameN;  // exact frame index
      
      text_152.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 120.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_152.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_152.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    planningpathstraining2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function planningpathstraining2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'planningpathstraining2' ---
    planningpathstraining2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('planningpathstraining2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (answer_quiz1_5.keys === undefined) {
      if (['None','none',undefined].includes(correct_answer2)) {
         answer_quiz1_5.corr = 1;  // correct non-response
      } else {
         answer_quiz1_5.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(answer_quiz1_5.corr, level);
    }
    psychoJS.experiment.addData('answer_quiz1_5.keys', answer_quiz1_5.keys);
    psychoJS.experiment.addData('answer_quiz1_5.corr', answer_quiz1_5.corr);
    if (typeof answer_quiz1_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('answer_quiz1_5.rt', answer_quiz1_5.rt);
        psychoJS.experiment.addData('answer_quiz1_5.duration', answer_quiz1_5.duration);
        routineTimer.reset();
        }
    
    answer_quiz1_5.stop();
    quiz1_count += 1;
    if (answer_quiz1_3.corr) {
        if (answer_quiz1_5.corr) {
              msg = "correct! well done";
              quiz_planning_corr += 1;
               }
     } 
    else {
         msg = "incorrect";
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var correct_forget_pathsComponents;
function correct_forget_pathsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'correct_forget_paths' ---
    t = 0;
    correct_forget_pathsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('correct_forget_paths.started', globalClock.getTime());
    next_trial_text_2.setText(msg);
    text_151.setText(quiz_planning_corr);
    // keep track of which components have finished
    correct_forget_pathsComponents = [];
    correct_forget_pathsComponents.push(next_trial_text_2);
    correct_forget_pathsComponents.push(text_151);
    
    correct_forget_pathsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function correct_forget_pathsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'correct_forget_paths' ---
    // get current time
    t = correct_forget_pathsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *next_trial_text_2* updates
    if (t >= 0.0 && next_trial_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_trial_text_2.tStart = t;  // (not accounting for frame time here)
      next_trial_text_2.frameNStart = frameN;  // exact frame index
      
      next_trial_text_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (next_trial_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      next_trial_text_2.setAutoDraw(false);
    }
    
    // *text_151* updates
    if (t >= 0.0 && text_151.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_151.tStart = t;  // (not accounting for frame time here)
      text_151.frameNStart = frameN;  // exact frame index
      
      text_151.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_151.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_151.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    correct_forget_pathsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function correct_forget_pathsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'correct_forget_paths' ---
    correct_forget_pathsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('correct_forget_paths.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var total_planning_score_training;
var total_score_planningComponents;
function total_score_planningRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'total_score_planning' ---
    t = 0;
    total_score_planningClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('total_score_planning.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_43
    total_planning_score_training = ((quiz_planning_corr / 8.0) * 100);
    psychoJS.experiment.addData("score_planning_training",total_planning_score_training);
    
    next_trial_text_3.setText(total_planning_score_training);
    // keep track of which components have finished
    total_score_planningComponents = [];
    total_score_planningComponents.push(next_trial_text_3);
    total_score_planningComponents.push(text_150);
    
    total_score_planningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function total_score_planningRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'total_score_planning' ---
    // get current time
    t = total_score_planningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *next_trial_text_3* updates
    if (t >= 0.0 && next_trial_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      next_trial_text_3.tStart = t;  // (not accounting for frame time here)
      next_trial_text_3.frameNStart = frameN;  // exact frame index
      
      next_trial_text_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (next_trial_text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      next_trial_text_3.setAutoDraw(false);
    }
    
    // *text_150* updates
    if (t >= 0.0 && text_150.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_150.tStart = t;  // (not accounting for frame time here)
      text_150.frameNStart = frameN;  // exact frame index
      
      text_150.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_150.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_150.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    total_score_planningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function total_score_planningRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'total_score_planning' ---
    total_score_planningComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('total_score_planning.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var break_routineComponents;
function break_routineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'break_routine' ---
    t = 0;
    break_routineClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('break_routine.started', globalClock.getTime());
    // keep track of which components have finished
    break_routineComponents = [];
    break_routineComponents.push(text_9);
    
    break_routineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function break_routineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'break_routine' ---
    // get current time
    t = break_routineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_9* updates
    if (t >= 0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }
    
    frameRemains = 0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_9.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    break_routineComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function break_routineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'break_routine' ---
    break_routineComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('break_routine.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_11_allKeys;
var instructions_rewardComponents;
function instructions_rewardRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_reward' ---
    t = 0;
    instructions_rewardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions_reward.started', globalClock.getTime());
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    // keep track of which components have finished
    instructions_rewardComponents = [];
    instructions_rewardComponents.push(instructions_rewardstage);
    instructions_rewardComponents.push(key_resp_11);
    instructions_rewardComponents.push(text_46);
    
    instructions_rewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_rewardRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_reward' ---
    // get current time
    t = instructions_rewardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_rewardstage* updates
    if (t >= 0.0 && instructions_rewardstage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_rewardstage.tStart = t;  // (not accounting for frame time here)
      instructions_rewardstage.frameNStart = frameN;  // exact frame index
      
      instructions_rewardstage.setAutoDraw(true);
    }
    
    
    // *key_resp_11* updates
    if (t >= 10.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }
    
    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        key_resp_11.duration = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_46* updates
    if (t >= 10.0 && text_46.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_46.tStart = t;  // (not accounting for frame time here)
      text_46.frameNStart = frameN;  // exact frame index
      
      text_46.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions_rewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_rewardRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_reward' ---
    instructions_rewardComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions_reward.stopped', globalClock.getTime());
    key_resp_11.stop();
    // the Routine "instructions_reward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_9_allKeys;
var instructions_planning_2Components;
function instructions_planning_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_planning_2' ---
    t = 0;
    instructions_planning_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions_planning_2.started', globalClock.getTime());
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // keep track of which components have finished
    instructions_planning_2Components = [];
    instructions_planning_2Components.push(text_50);
    instructions_planning_2Components.push(key_resp_9);
    
    instructions_planning_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_planning_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_planning_2' ---
    // get current time
    t = instructions_planning_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_50* updates
    if (t >= 0.0 && text_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_50.tStart = t;  // (not accounting for frame time here)
      text_50.frameNStart = frameN;  // exact frame index
      
      text_50.setAutoDraw(true);
    }
    
    
    // *key_resp_9* updates
    if (t >= 0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }
    
    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        key_resp_9.duration = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions_planning_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_planning_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_planning_2' ---
    instructions_planning_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions_planning_2.stopped', globalClock.getTime());
    key_resp_9.stop();
    // the Routine "instructions_planning_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var al1;
var al2;
var _plan2_response_2_allKeys;
var instructions_example_trialComponents;
function instructions_example_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_example_trial' ---
    t = 0;
    instructions_example_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(30.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions_example_trial.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_13
    al1=400
    al2=50
    plan2_response_2.keys = undefined;
    plan2_response_2.rt = undefined;
    _plan2_response_2_allKeys = [];
    // keep track of which components have finished
    instructions_example_trialComponents = [];
    instructions_example_trialComponents.push(text_13);
    instructions_example_trialComponents.push(R1_5);
    instructions_example_trialComponents.push(R2_5);
    instructions_example_trialComponents.push(rew1_5);
    instructions_example_trialComponents.push(rew2_5);
    instructions_example_trialComponents.push(text_21);
    instructions_example_trialComponents.push(plan2_response_2);
    instructions_example_trialComponents.push(current_image_decision2_2);
    
    instructions_example_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_example_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_example_trial' ---
    // get current time
    t = instructions_example_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_13* updates
    if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_13.tStart = t;  // (not accounting for frame time here)
      text_13.frameNStart = frameN;  // exact frame index
      
      text_13.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_13.setAutoDraw(false);
    }
    
    // *R1_5* updates
    if (t >= 0.0 && R1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R1_5.tStart = t;  // (not accounting for frame time here)
      R1_5.frameNStart = frameN;  // exact frame index
      
      R1_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R1_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R1_5.setAutoDraw(false);
    }
    
    // *R2_5* updates
    if (t >= 0.0 && R2_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_5.tStart = t;  // (not accounting for frame time here)
      R2_5.frameNStart = frameN;  // exact frame index
      
      R2_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_5.setAutoDraw(false);
    }
    
    if (rew1_5.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew1_5.setText(al1, false);
    }
    
    // *rew1_5* updates
    if (t >= 0.0 && rew1_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew1_5.tStart = t;  // (not accounting for frame time here)
      rew1_5.frameNStart = frameN;  // exact frame index
      
      rew1_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew1_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew1_5.setAutoDraw(false);
    }
    
    if (rew2_5.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew2_5.setText('SPACE: Win 100\n', false);
    }
    
    // *rew2_5* updates
    if (t >= 0.0 && rew2_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew2_5.tStart = t;  // (not accounting for frame time here)
      rew2_5.frameNStart = frameN;  // exact frame index
      
      rew2_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew2_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew2_5.setAutoDraw(false);
    }
    
    // *text_21* updates
    if (t >= 0.0 && text_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_21.tStart = t;  // (not accounting for frame time here)
      text_21.frameNStart = frameN;  // exact frame index
      
      text_21.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_21.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_21.setAutoDraw(false);
    }
    
    // *plan2_response_2* updates
    if (t >= 0.0 && plan2_response_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plan2_response_2.tStart = t;  // (not accounting for frame time here)
      plan2_response_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { plan2_response_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_2.clearEvents(); });
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (plan2_response_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      plan2_response_2.status = PsychoJS.Status.FINISHED;
        }
      
    if (plan2_response_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = plan2_response_2.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _plan2_response_2_allKeys = _plan2_response_2_allKeys.concat(theseKeys);
      if (_plan2_response_2_allKeys.length > 0) {
        plan2_response_2.keys = _plan2_response_2_allKeys[_plan2_response_2_allKeys.length - 1].name;  // just the last key pressed
        plan2_response_2.rt = _plan2_response_2_allKeys[_plan2_response_2_allKeys.length - 1].rt;
        plan2_response_2.duration = _plan2_response_2_allKeys[_plan2_response_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *current_image_decision2_2* updates
    if (t >= 0.0 && current_image_decision2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      current_image_decision2_2.tStart = t;  // (not accounting for frame time here)
      current_image_decision2_2.frameNStart = frameN;  // exact frame index
      
      current_image_decision2_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (current_image_decision2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      current_image_decision2_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions_example_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_example_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_example_trial' ---
    instructions_example_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions_example_trial.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(plan2_response_2.corr, level);
    }
    psychoJS.experiment.addData('plan2_response_2.keys', plan2_response_2.keys);
    if (typeof plan2_response_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('plan2_response_2.rt', plan2_response_2.rt);
        psychoJS.experiment.addData('plan2_response_2.duration', plan2_response_2.duration);
        routineTimer.reset();
        }
    
    plan2_response_2.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_12_allKeys;
var long_term_reward_instructionsComponents;
function long_term_reward_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'long_term_reward_instructions' ---
    t = 0;
    long_term_reward_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('long_term_reward_instructions.started', globalClock.getTime());
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    // keep track of which components have finished
    long_term_reward_instructionsComponents = [];
    long_term_reward_instructionsComponents.push(instructions_rewardstage_2);
    long_term_reward_instructionsComponents.push(key_resp_12);
    long_term_reward_instructionsComponents.push(text_45);
    
    long_term_reward_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function long_term_reward_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'long_term_reward_instructions' ---
    // get current time
    t = long_term_reward_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_rewardstage_2* updates
    if (t >= 0.0 && instructions_rewardstage_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_rewardstage_2.tStart = t;  // (not accounting for frame time here)
      instructions_rewardstage_2.frameNStart = frameN;  // exact frame index
      
      instructions_rewardstage_2.setAutoDraw(true);
    }
    
    
    // *key_resp_12* updates
    if (t >= 10.0 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }
    
    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        key_resp_12.duration = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_45* updates
    if (t >= 10.0 && text_45.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_45.tStart = t;  // (not accounting for frame time here)
      text_45.frameNStart = frameN;  // exact frame index
      
      text_45.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    long_term_reward_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function long_term_reward_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'long_term_reward_instructions' ---
    long_term_reward_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('long_term_reward_instructions.stopped', globalClock.getTime());
    key_resp_12.stop();
    // the Routine "long_term_reward_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_21_allKeys;
var quiz_planning_1Components;
function quiz_planning_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz_planning_1' ---
    t = 0;
    quiz_planning_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz_planning_1.started', globalClock.getTime());
    key_resp_21.keys = undefined;
    key_resp_21.rt = undefined;
    _key_resp_21_allKeys = [];
    // keep track of which components have finished
    quiz_planning_1Components = [];
    quiz_planning_1Components.push(text_47);
    quiz_planning_1Components.push(key_resp_21);
    
    quiz_planning_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz_planning_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz_planning_1' ---
    // get current time
    t = quiz_planning_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_47* updates
    if (t >= 0.0 && text_47.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_47.tStart = t;  // (not accounting for frame time here)
      text_47.frameNStart = frameN;  // exact frame index
      
      text_47.setAutoDraw(true);
    }
    
    
    // *key_resp_21* updates
    if (t >= 0.0 && key_resp_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_21.tStart = t;  // (not accounting for frame time here)
      key_resp_21.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_21.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_21.clearEvents(); });
    }
    
    if (key_resp_21.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_21.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_21_allKeys = _key_resp_21_allKeys.concat(theseKeys);
      if (_key_resp_21_allKeys.length > 0) {
        key_resp_21.keys = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].name;  // just the last key pressed
        key_resp_21.rt = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].rt;
        key_resp_21.duration = _key_resp_21_allKeys[_key_resp_21_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz_planning_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_planning_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz_planning_1' ---
    quiz_planning_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz_planning_1.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_28
    correct = 0;
    if ((key_resp_21.keys === "c")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_21.corr, level);
    }
    psychoJS.experiment.addData('key_resp_21.keys', key_resp_21.keys);
    if (typeof key_resp_21.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_21.rt', key_resp_21.rt);
        psychoJS.experiment.addData('key_resp_21.duration', key_resp_21.duration);
        routineTimer.reset();
        }
    
    key_resp_21.stop();
    // the Routine "quiz_planning_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_22_allKeys;
var quiz_planning_2Components;
function quiz_planning_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz_planning_2' ---
    t = 0;
    quiz_planning_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz_planning_2.started', globalClock.getTime());
    key_resp_22.keys = undefined;
    key_resp_22.rt = undefined;
    _key_resp_22_allKeys = [];
    // keep track of which components have finished
    quiz_planning_2Components = [];
    quiz_planning_2Components.push(text_73);
    quiz_planning_2Components.push(key_resp_22);
    
    quiz_planning_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz_planning_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz_planning_2' ---
    // get current time
    t = quiz_planning_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_73* updates
    if (t >= 0.0 && text_73.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_73.tStart = t;  // (not accounting for frame time here)
      text_73.frameNStart = frameN;  // exact frame index
      
      text_73.setAutoDraw(true);
    }
    
    
    // *key_resp_22* updates
    if (t >= 0.0 && key_resp_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_22.tStart = t;  // (not accounting for frame time here)
      key_resp_22.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_22.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.clearEvents(); });
    }
    
    if (key_resp_22.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_22.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_22_allKeys = _key_resp_22_allKeys.concat(theseKeys);
      if (_key_resp_22_allKeys.length > 0) {
        key_resp_22.keys = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].name;  // just the last key pressed
        key_resp_22.rt = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].rt;
        key_resp_22.duration = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz_planning_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_planning_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz_planning_2' ---
    quiz_planning_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz_planning_2.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_32
    if ((key_resp_22.keys === "b")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_22.corr, level);
    }
    psychoJS.experiment.addData('key_resp_22.keys', key_resp_22.keys);
    if (typeof key_resp_22.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_22.rt', key_resp_22.rt);
        psychoJS.experiment.addData('key_resp_22.duration', key_resp_22.duration);
        routineTimer.reset();
        }
    
    key_resp_22.stop();
    // the Routine "quiz_planning_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_24_allKeys;
var quiz_planning_3Components;
function quiz_planning_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz_planning_3' ---
    t = 0;
    quiz_planning_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('quiz_planning_3.started', globalClock.getTime());
    key_resp_24.keys = undefined;
    key_resp_24.rt = undefined;
    _key_resp_24_allKeys = [];
    // keep track of which components have finished
    quiz_planning_3Components = [];
    quiz_planning_3Components.push(text_74);
    quiz_planning_3Components.push(key_resp_24);
    
    quiz_planning_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz_planning_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz_planning_3' ---
    // get current time
    t = quiz_planning_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_74* updates
    if (t >= 0.0 && text_74.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_74.tStart = t;  // (not accounting for frame time here)
      text_74.frameNStart = frameN;  // exact frame index
      
      text_74.setAutoDraw(true);
    }
    
    
    // *key_resp_24* updates
    if (t >= 0.0 && key_resp_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_24.tStart = t;  // (not accounting for frame time here)
      key_resp_24.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_24.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_24.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_24.clearEvents(); });
    }
    
    if (key_resp_24.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_24.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_24_allKeys = _key_resp_24_allKeys.concat(theseKeys);
      if (_key_resp_24_allKeys.length > 0) {
        key_resp_24.keys = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].name;  // just the last key pressed
        key_resp_24.rt = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].rt;
        key_resp_24.duration = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    quiz_planning_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_planning_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz_planning_3' ---
    quiz_planning_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('quiz_planning_3.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_36
    if ((key_resp_24.keys === "b")) {
        correct += 1;
    }
    if ((correct === 3)) {
        instructions_planning_get_right.finished = true;
        msg = "Correct! You can now move on";
    } else {
        msg = "Incorrect! You need to repeat the instructions.";
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_24.corr, level);
    }
    psychoJS.experiment.addData('key_resp_24.keys', key_resp_24.keys);
    if (typeof key_resp_24.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_24.rt', key_resp_24.rt);
        psychoJS.experiment.addData('key_resp_24.duration', key_resp_24.duration);
        routineTimer.reset();
        }
    
    key_resp_24.stop();
    // the Routine "quiz_planning_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_8_allKeys;
var total_practice_planning;
var w2;
var see_planning_trialsComponents;
function see_planning_trialsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'see_planning_trials' ---
    t = 0;
    see_planning_trialsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('see_planning_trials.started', globalClock.getTime());
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // Run 'Begin Routine' code from code_12
    total_practice_planning = 0;
    w2 = 400;
    
    // keep track of which components have finished
    see_planning_trialsComponents = [];
    see_planning_trialsComponents.push(text_48);
    see_planning_trialsComponents.push(key_resp_8);
    
    see_planning_trialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function see_planning_trialsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'see_planning_trials' ---
    // get current time
    t = see_planning_trialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_48* updates
    if (t >= 0.0 && text_48.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_48.tStart = t;  // (not accounting for frame time here)
      text_48.frameNStart = frameN;  // exact frame index
      
      text_48.setAutoDraw(true);
    }
    
    
    // *key_resp_8* updates
    if (t >= 0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }
    
    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        key_resp_8.duration = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    see_planning_trialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function see_planning_trialsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'see_planning_trials' ---
    see_planning_trialsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('see_planning_trials.stopped', globalClock.getTime());
    key_resp_8.stop();
    // the Routine "see_planning_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var planning_total;
var _plan2_response_3_allKeys;
var instructions_planning_newComponents;
function instructions_planning_newRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_planning_new' ---
    t = 0;
    instructions_planning_newClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions_planning_new.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_15
    al1=400
    w2=400
    
    planning_total="Total = 0";
    plan2_response_3.keys = undefined;
    plan2_response_3.rt = undefined;
    _plan2_response_3_allKeys = [];
    text_114.setText(total_practice_planning);
    // keep track of which components have finished
    instructions_planning_newComponents = [];
    instructions_planning_newComponents.push(text_32);
    instructions_planning_newComponents.push(R1_6);
    instructions_planning_newComponents.push(R2_6);
    instructions_planning_newComponents.push(rew1_6);
    instructions_planning_newComponents.push(rew2_6);
    instructions_planning_newComponents.push(plan2_response_3);
    instructions_planning_newComponents.push(text_34);
    instructions_planning_newComponents.push(text_41);
    instructions_planning_newComponents.push(text_114);
    instructions_planning_newComponents.push(text_128);
    
    instructions_planning_newComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_planning_newRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_planning_new' ---
    // get current time
    t = instructions_planning_newClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_32* updates
    if (t >= 0.0 && text_32.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_32.tStart = t;  // (not accounting for frame time here)
      text_32.frameNStart = frameN;  // exact frame index
      
      text_32.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_32.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_32.setAutoDraw(false);
    }
    
    // *R1_6* updates
    if (t >= 0.0 && R1_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R1_6.tStart = t;  // (not accounting for frame time here)
      R1_6.frameNStart = frameN;  // exact frame index
      
      R1_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R1_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R1_6.setAutoDraw(false);
    }
    
    // *R2_6* updates
    if (t >= 0.0 && R2_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_6.tStart = t;  // (not accounting for frame time here)
      R2_6.frameNStart = frameN;  // exact frame index
      
      R2_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_6.setAutoDraw(false);
    }
    
    if (rew1_6.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew1_6.setText('SPACE for 100', false);
    }
    
    // *rew1_6* updates
    if (t >= 0.0 && rew1_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew1_6.tStart = t;  // (not accounting for frame time here)
      rew1_6.frameNStart = frameN;  // exact frame index
      
      rew1_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew1_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew1_6.setAutoDraw(false);
    }
    
    if (rew2_6.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew2_6.setText(w2, false);
    }
    
    // *rew2_6* updates
    if (t >= 0.0 && rew2_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew2_6.tStart = t;  // (not accounting for frame time here)
      rew2_6.frameNStart = frameN;  // exact frame index
      
      rew2_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew2_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew2_6.setAutoDraw(false);
    }
    
    // *plan2_response_3* updates
    if (t >= 0.0 && plan2_response_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plan2_response_3.tStart = t;  // (not accounting for frame time here)
      plan2_response_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { plan2_response_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_3.clearEvents(); });
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (plan2_response_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      plan2_response_3.status = PsychoJS.Status.FINISHED;
        }
      
    if (plan2_response_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = plan2_response_3.getKeys({keyList: ['space'], waitRelease: false});
      _plan2_response_3_allKeys = _plan2_response_3_allKeys.concat(theseKeys);
      if (_plan2_response_3_allKeys.length > 0) {
        plan2_response_3.keys = _plan2_response_3_allKeys[_plan2_response_3_allKeys.length - 1].name;  // just the last key pressed
        plan2_response_3.rt = _plan2_response_3_allKeys[_plan2_response_3_allKeys.length - 1].rt;
        plan2_response_3.duration = _plan2_response_3_allKeys[_plan2_response_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_34* updates
    if (t >= 0.0 && text_34.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_34.tStart = t;  // (not accounting for frame time here)
      text_34.frameNStart = frameN;  // exact frame index
      
      text_34.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_34.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_34.setAutoDraw(false);
    }
    
    // *text_41* updates
    if (t >= 0.0 && text_41.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_41.tStart = t;  // (not accounting for frame time here)
      text_41.frameNStart = frameN;  // exact frame index
      
      text_41.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_41.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_41.setAutoDraw(false);
    }
    
    // *text_114* updates
    if (t >= 0.0 && text_114.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_114.tStart = t;  // (not accounting for frame time here)
      text_114.frameNStart = frameN;  // exact frame index
      
      text_114.setAutoDraw(true);
    }
    
    
    // *text_128* updates
    if (t >= 0.0 && text_128.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_128.tStart = t;  // (not accounting for frame time here)
      text_128.frameNStart = frameN;  // exact frame index
      
      text_128.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions_planning_newComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_planning_newRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_planning_new' ---
    instructions_planning_newComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions_planning_new.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(plan2_response_3.corr, level);
    }
    psychoJS.experiment.addData('plan2_response_3.keys', plan2_response_3.keys);
    if (typeof plan2_response_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('plan2_response_3.rt', plan2_response_3.rt);
        psychoJS.experiment.addData('plan2_response_3.duration', plan2_response_3.duration);
        routineTimer.reset();
        }
    
    plan2_response_3.stop();
    // the Routine "instructions_planning_new" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _plan2_response_6_allKeys;
var planning_2_instructionsComponents;
function planning_2_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'planning_2_instructions' ---
    t = 0;
    planning_2_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('planning_2_instructions.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_23
    total_practice_planning = (total_practice_planning + 100);
    
    plan2_response_6.keys = undefined;
    plan2_response_6.rt = undefined;
    _plan2_response_6_allKeys = [];
    text_115.setText(total_practice_planning);
    // keep track of which components have finished
    planning_2_instructionsComponents = [];
    planning_2_instructionsComponents.push(text_52);
    planning_2_instructionsComponents.push(R1_9);
    planning_2_instructionsComponents.push(R2_9);
    planning_2_instructionsComponents.push(rew1_9);
    planning_2_instructionsComponents.push(rew2_9);
    planning_2_instructionsComponents.push(text_53);
    planning_2_instructionsComponents.push(plan2_response_6);
    planning_2_instructionsComponents.push(current_image_decision2_5);
    planning_2_instructionsComponents.push(text_115);
    planning_2_instructionsComponents.push(text_129);
    
    planning_2_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function planning_2_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'planning_2_instructions' ---
    // get current time
    t = planning_2_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_52* updates
    if (t >= 0.0 && text_52.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_52.tStart = t;  // (not accounting for frame time here)
      text_52.frameNStart = frameN;  // exact frame index
      
      text_52.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_52.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_52.setAutoDraw(false);
    }
    
    // *R1_9* updates
    if (t >= 0.0 && R1_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R1_9.tStart = t;  // (not accounting for frame time here)
      R1_9.frameNStart = frameN;  // exact frame index
      
      R1_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R1_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R1_9.setAutoDraw(false);
    }
    
    // *R2_9* updates
    if (t >= 0.0 && R2_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_9.tStart = t;  // (not accounting for frame time here)
      R2_9.frameNStart = frameN;  // exact frame index
      
      R2_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_9.setAutoDraw(false);
    }
    
    if (rew1_9.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew1_9.setText('SPACE for 100', false);
    }
    
    // *rew1_9* updates
    if (t >= 0.0 && rew1_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew1_9.tStart = t;  // (not accounting for frame time here)
      rew1_9.frameNStart = frameN;  // exact frame index
      
      rew1_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew1_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew1_9.setAutoDraw(false);
    }
    
    if (rew2_9.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew2_9.setText(w2, false);
    }
    
    // *rew2_9* updates
    if (t >= 0.0 && rew2_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew2_9.tStart = t;  // (not accounting for frame time here)
      rew2_9.frameNStart = frameN;  // exact frame index
      
      rew2_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew2_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew2_9.setAutoDraw(false);
    }
    
    // *text_53* updates
    if (t >= 0.0 && text_53.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_53.tStart = t;  // (not accounting for frame time here)
      text_53.frameNStart = frameN;  // exact frame index
      
      text_53.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_53.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_53.setAutoDraw(false);
    }
    
    // *plan2_response_6* updates
    if (t >= 0.0 && plan2_response_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plan2_response_6.tStart = t;  // (not accounting for frame time here)
      plan2_response_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { plan2_response_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_6.clearEvents(); });
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (plan2_response_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      plan2_response_6.status = PsychoJS.Status.FINISHED;
        }
      
    if (plan2_response_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = plan2_response_6.getKeys({keyList: ['space'], waitRelease: false});
      _plan2_response_6_allKeys = _plan2_response_6_allKeys.concat(theseKeys);
      if (_plan2_response_6_allKeys.length > 0) {
        plan2_response_6.keys = _plan2_response_6_allKeys[_plan2_response_6_allKeys.length - 1].name;  // just the last key pressed
        plan2_response_6.rt = _plan2_response_6_allKeys[_plan2_response_6_allKeys.length - 1].rt;
        plan2_response_6.duration = _plan2_response_6_allKeys[_plan2_response_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *current_image_decision2_5* updates
    if (t >= 0.0 && current_image_decision2_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      current_image_decision2_5.tStart = t;  // (not accounting for frame time here)
      current_image_decision2_5.frameNStart = frameN;  // exact frame index
      
      current_image_decision2_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (current_image_decision2_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      current_image_decision2_5.setAutoDraw(false);
    }
    
    // *text_115* updates
    if (t >= 0.0 && text_115.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_115.tStart = t;  // (not accounting for frame time here)
      text_115.frameNStart = frameN;  // exact frame index
      
      text_115.setAutoDraw(true);
    }
    
    
    // *text_129* updates
    if (t >= 0.0 && text_129.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_129.tStart = t;  // (not accounting for frame time here)
      text_129.frameNStart = frameN;  // exact frame index
      
      text_129.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    planning_2_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function planning_2_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'planning_2_instructions' ---
    planning_2_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('planning_2_instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(plan2_response_6.corr, level);
    }
    psychoJS.experiment.addData('plan2_response_6.keys', plan2_response_6.keys);
    if (typeof plan2_response_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('plan2_response_6.rt', plan2_response_6.rt);
        psychoJS.experiment.addData('plan2_response_6.duration', plan2_response_6.duration);
        routineTimer.reset();
        }
    
    plan2_response_6.stop();
    // the Routine "planning_2_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _plan2_response_5_allKeys;
var instructions_planning_new3Components;
function instructions_planning_new3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_planning_new3' ---
    t = 0;
    instructions_planning_new3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions_planning_new3.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_29
    total_practice_planning = total_practice_planning;
    
    plan2_response_5.keys = undefined;
    plan2_response_5.rt = undefined;
    _plan2_response_5_allKeys = [];
    text_139.setText(total_practice_planning);
    // keep track of which components have finished
    instructions_planning_new3Components = [];
    instructions_planning_new3Components.push(text_136);
    instructions_planning_new3Components.push(R1_11);
    instructions_planning_new3Components.push(R2_11);
    instructions_planning_new3Components.push(rew1_11);
    instructions_planning_new3Components.push(rew2_11);
    instructions_planning_new3Components.push(plan2_response_5);
    instructions_planning_new3Components.push(current_image_decision2_6);
    instructions_planning_new3Components.push(text_137);
    instructions_planning_new3Components.push(text_138);
    instructions_planning_new3Components.push(text_139);
    instructions_planning_new3Components.push(text_140);
    
    instructions_planning_new3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_planning_new3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_planning_new3' ---
    // get current time
    t = instructions_planning_new3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_136* updates
    if (t >= 0.0 && text_136.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_136.tStart = t;  // (not accounting for frame time here)
      text_136.frameNStart = frameN;  // exact frame index
      
      text_136.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_136.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_136.setAutoDraw(false);
    }
    
    // *R1_11* updates
    if (t >= 0.0 && R1_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R1_11.tStart = t;  // (not accounting for frame time here)
      R1_11.frameNStart = frameN;  // exact frame index
      
      R1_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R1_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R1_11.setAutoDraw(false);
    }
    
    // *R2_11* updates
    if (t >= 0.0 && R2_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_11.tStart = t;  // (not accounting for frame time here)
      R2_11.frameNStart = frameN;  // exact frame index
      
      R2_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (R2_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      R2_11.setAutoDraw(false);
    }
    
    if (rew1_11.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew1_11.setText('SPACE for 100', false);
    }
    
    // *rew1_11* updates
    if (t >= 0.0 && rew1_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew1_11.tStart = t;  // (not accounting for frame time here)
      rew1_11.frameNStart = frameN;  // exact frame index
      
      rew1_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew1_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew1_11.setAutoDraw(false);
    }
    
    if (rew2_11.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew2_11.setText(w2, false);
    }
    
    // *rew2_11* updates
    if (t >= 0.0 && rew2_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew2_11.tStart = t;  // (not accounting for frame time here)
      rew2_11.frameNStart = frameN;  // exact frame index
      
      rew2_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rew2_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rew2_11.setAutoDraw(false);
    }
    
    // *plan2_response_5* updates
    if (t >= 0.0 && plan2_response_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plan2_response_5.tStart = t;  // (not accounting for frame time here)
      plan2_response_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { plan2_response_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { plan2_response_5.clearEvents(); });
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (plan2_response_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      plan2_response_5.status = PsychoJS.Status.FINISHED;
        }
      
    if (plan2_response_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = plan2_response_5.getKeys({keyList: ['right', 'space', 'left'], waitRelease: false});
      _plan2_response_5_allKeys = _plan2_response_5_allKeys.concat(theseKeys);
      if (_plan2_response_5_allKeys.length > 0) {
        plan2_response_5.keys = _plan2_response_5_allKeys[_plan2_response_5_allKeys.length - 1].name;  // just the last key pressed
        plan2_response_5.rt = _plan2_response_5_allKeys[_plan2_response_5_allKeys.length - 1].rt;
        plan2_response_5.duration = _plan2_response_5_allKeys[_plan2_response_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *current_image_decision2_6* updates
    if (t >= 0.0 && current_image_decision2_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      current_image_decision2_6.tStart = t;  // (not accounting for frame time here)
      current_image_decision2_6.frameNStart = frameN;  // exact frame index
      
      current_image_decision2_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (current_image_decision2_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      current_image_decision2_6.setAutoDraw(false);
    }
    
    // *text_137* updates
    if (t >= 0.0 && text_137.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_137.tStart = t;  // (not accounting for frame time here)
      text_137.frameNStart = frameN;  // exact frame index
      
      text_137.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_137.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_137.setAutoDraw(false);
    }
    
    // *text_138* updates
    if (t >= 0.0 && text_138.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_138.tStart = t;  // (not accounting for frame time here)
      text_138.frameNStart = frameN;  // exact frame index
      
      text_138.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_138.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_138.setAutoDraw(false);
    }
    
    // *text_139* updates
    if (t >= 0.0 && text_139.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_139.tStart = t;  // (not accounting for frame time here)
      text_139.frameNStart = frameN;  // exact frame index
      
      text_139.setAutoDraw(true);
    }
    
    
    // *text_140* updates
    if (t >= 0.0 && text_140.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_140.tStart = t;  // (not accounting for frame time here)
      text_140.frameNStart = frameN;  // exact frame index
      
      text_140.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructions_planning_new3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_planning_new3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_planning_new3' ---
    instructions_planning_new3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions_planning_new3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(plan2_response_5.corr, level);
    }
    psychoJS.experiment.addData('plan2_response_5.keys', plan2_response_5.keys);
    if (typeof plan2_response_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('plan2_response_5.rt', plan2_response_5.rt);
        psychoJS.experiment.addData('plan2_response_5.duration', plan2_response_5.duration);
        routineTimer.reset();
        }
    
    plan2_response_5.stop();
    // the Routine "instructions_planning_new3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_planning_outcomesComponents;
function practice_planning_outcomesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_planning_outcomes' ---
    t = 0;
    practice_planning_outcomesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_planning_outcomes.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_33
    total_practice_planning += 400;
    
    text_142.setText(total_practice_planning);
    // keep track of which components have finished
    practice_planning_outcomesComponents = [];
    practice_planning_outcomesComponents.push(image_6);
    practice_planning_outcomesComponents.push(text_141);
    practice_planning_outcomesComponents.push(text_142);
    practice_planning_outcomesComponents.push(text_143);
    
    practice_planning_outcomesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_planning_outcomesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_planning_outcomes' ---
    // get current time
    t = practice_planning_outcomesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_6* updates
    if (t >= 0.0 && image_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_6.tStart = t;  // (not accounting for frame time here)
      image_6.frameNStart = frameN;  // exact frame index
      
      image_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_6.setAutoDraw(false);
    }
    
    // *text_141* updates
    if (t >= 0.0 && text_141.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_141.tStart = t;  // (not accounting for frame time here)
      text_141.frameNStart = frameN;  // exact frame index
      
      text_141.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_141.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_141.setAutoDraw(false);
    }
    
    // *text_142* updates
    if (t >= 0.0 && text_142.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_142.tStart = t;  // (not accounting for frame time here)
      text_142.frameNStart = frameN;  // exact frame index
      
      text_142.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_142.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_142.setAutoDraw(false);
    }
    
    // *text_143* updates
    if (t >= 0.0 && text_143.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_143.tStart = t;  // (not accounting for frame time here)
      text_143.frameNStart = frameN;  // exact frame index
      
      text_143.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_143.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_143.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_planning_outcomesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_planning_outcomesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_planning_outcomes' ---
    practice_planning_outcomesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice_planning_outcomes.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_39_allKeys;
var immediate_rewar_lessonComponents;
function immediate_rewar_lessonRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'immediate_rewar_lesson' ---
    t = 0;
    immediate_rewar_lessonClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('immediate_rewar_lesson.started', globalClock.getTime());
    key_resp_39.keys = undefined;
    key_resp_39.rt = undefined;
    _key_resp_39_allKeys = [];
    // Run 'Begin Routine' code from code_41
    total_practice_planning = 0;
    
    // keep track of which components have finished
    immediate_rewar_lessonComponents = [];
    immediate_rewar_lessonComponents.push(text_148);
    immediate_rewar_lessonComponents.push(key_resp_39);
    
    immediate_rewar_lessonComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function immediate_rewar_lessonRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'immediate_rewar_lesson' ---
    // get current time
    t = immediate_rewar_lessonClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_148* updates
    if (t >= 0.0 && text_148.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_148.tStart = t;  // (not accounting for frame time here)
      text_148.frameNStart = frameN;  // exact frame index
      
      text_148.setAutoDraw(true);
    }
    
    
    // *key_resp_39* updates
    if (t >= 0 && key_resp_39.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_39.tStart = t;  // (not accounting for frame time here)
      key_resp_39.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_39.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_39.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_39.clearEvents(); });
    }
    
    if (key_resp_39.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_39.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_39_allKeys = _key_resp_39_allKeys.concat(theseKeys);
      if (_key_resp_39_allKeys.length > 0) {
        key_resp_39.keys = _key_resp_39_allKeys[_key_resp_39_allKeys.length - 1].name;  // just the last key pressed
        key_resp_39.rt = _key_resp_39_allKeys[_key_resp_39_allKeys.length - 1].rt;
        key_resp_39.duration = _key_resp_39_allKeys[_key_resp_39_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    immediate_rewar_lessonComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function immediate_rewar_lessonRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'immediate_rewar_lesson' ---
    immediate_rewar_lessonComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('immediate_rewar_lesson.stopped', globalClock.getTime());
    key_resp_39.stop();
    // the Routine "immediate_rewar_lesson" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_37_allKeys;
var lesson_practiceComponents;
function lesson_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lesson_practice' ---
    t = 0;
    lesson_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lesson_practice.started', globalClock.getTime());
    key_resp_37.keys = undefined;
    key_resp_37.rt = undefined;
    _key_resp_37_allKeys = [];
    // Run 'Begin Routine' code from code_34
    total_practice_planning = 0;
    
    // keep track of which components have finished
    lesson_practiceComponents = [];
    lesson_practiceComponents.push(text_144);
    lesson_practiceComponents.push(key_resp_37);
    
    lesson_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function lesson_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lesson_practice' ---
    // get current time
    t = lesson_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_144* updates
    if (t >= 0.0 && text_144.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_144.tStart = t;  // (not accounting for frame time here)
      text_144.frameNStart = frameN;  // exact frame index
      
      text_144.setAutoDraw(true);
    }
    
    
    // *key_resp_37* updates
    if (t >= 0 && key_resp_37.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_37.tStart = t;  // (not accounting for frame time here)
      key_resp_37.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_37.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_37.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_37.clearEvents(); });
    }
    
    if (key_resp_37.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_37.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_37_allKeys = _key_resp_37_allKeys.concat(theseKeys);
      if (_key_resp_37_allKeys.length > 0) {
        key_resp_37.keys = _key_resp_37_allKeys[_key_resp_37_allKeys.length - 1].name;  // just the last key pressed
        key_resp_37.rt = _key_resp_37_allKeys[_key_resp_37_allKeys.length - 1].rt;
        key_resp_37.duration = _key_resp_37_allKeys[_key_resp_37_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    lesson_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lesson_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lesson_practice' ---
    lesson_practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('lesson_practice.stopped', globalClock.getTime());
    key_resp_37.stop();
    // the Routine "lesson_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_38_allKeys;
var lesson_practice_2Components;
function lesson_practice_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lesson_practice_2' ---
    t = 0;
    lesson_practice_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lesson_practice_2.started', globalClock.getTime());
    key_resp_38.keys = undefined;
    key_resp_38.rt = undefined;
    _key_resp_38_allKeys = [];
    // Run 'Begin Routine' code from code_37
    total_practice_planning = 0;
    
    // keep track of which components have finished
    lesson_practice_2Components = [];
    lesson_practice_2Components.push(text_145);
    lesson_practice_2Components.push(key_resp_38);
    
    lesson_practice_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function lesson_practice_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lesson_practice_2' ---
    // get current time
    t = lesson_practice_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_145* updates
    if (t >= 0.0 && text_145.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_145.tStart = t;  // (not accounting for frame time here)
      text_145.frameNStart = frameN;  // exact frame index
      
      text_145.setAutoDraw(true);
    }
    
    
    // *key_resp_38* updates
    if (t >= 0 && key_resp_38.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_38.tStart = t;  // (not accounting for frame time here)
      key_resp_38.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_38.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_38.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_38.clearEvents(); });
    }
    
    if (key_resp_38.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_38.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_38_allKeys = _key_resp_38_allKeys.concat(theseKeys);
      if (_key_resp_38_allKeys.length > 0) {
        key_resp_38.keys = _key_resp_38_allKeys[_key_resp_38_allKeys.length - 1].name;  // just the last key pressed
        key_resp_38.rt = _key_resp_38_allKeys[_key_resp_38_allKeys.length - 1].rt;
        key_resp_38.duration = _key_resp_38_allKeys[_key_resp_38_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    lesson_practice_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lesson_practice_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lesson_practice_2' ---
    lesson_practice_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('lesson_practice_2.stopped', globalClock.getTime());
    key_resp_38.stop();
    // the Routine "lesson_practice_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_6_allKeys;
var total_planning;
var start_real_planningComponents;
function start_real_planningRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_real_planning' ---
    t = 0;
    start_real_planningClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('start_real_planning.started', globalClock.getTime());
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // Run 'Begin Routine' code from code_17
    total_planning = 0;
    
    // keep track of which components have finished
    start_real_planningComponents = [];
    start_real_planningComponents.push(text_42);
    start_real_planningComponents.push(key_resp_6);
    
    start_real_planningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function start_real_planningRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_real_planning' ---
    // get current time
    t = start_real_planningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_42* updates
    if (t >= 0.0 && text_42.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_42.tStart = t;  // (not accounting for frame time here)
      text_42.frameNStart = frameN;  // exact frame index
      
      text_42.setAutoDraw(true);
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    start_real_planningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_real_planningRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_real_planning' ---
    start_real_planningComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('start_real_planning.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "start_real_planning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _plan1_response_allKeys;
var plan1_info_2Components;
function plan1_info_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'plan1_info_2' ---
    t = 0;
    plan1_info_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('plan1_info_2.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_5
    w2 = 400;
    
    R2.setImage(r2);
    plan1_response.keys = undefined;
    plan1_response.rt = undefined;
    _plan1_response_allKeys = [];
    text_117.setText(total_planning);
    // keep track of which components have finished
    plan1_info_2Components = [];
    plan1_info_2Components.push(text_5);
    plan1_info_2Components.push(R1);
    plan1_info_2Components.push(R2);
    plan1_info_2Components.push(rew1);
    plan1_info_2Components.push(rew2);
    plan1_info_2Components.push(text_6);
    plan1_info_2Components.push(plan1_response);
    plan1_info_2Components.push(babyleft);
    plan1_info_2Components.push(toothbrushright);
    plan1_info_2Components.push(text_117);
    plan1_info_2Components.push(text_120);
    
    plan1_info_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function plan1_info_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'plan1_info_2' ---
    // get current time
    t = plan1_info_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // *R1* updates
    if (t >= 0.0 && R1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R1.tStart = t;  // (not accounting for frame time here)
      R1.frameNStart = frameN;  // exact frame index
      
      R1.setAutoDraw(true);
    }
    
    
    // *R2* updates
    if (t >= 0.0 && R2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2.tStart = t;  // (not accounting for frame time here)
      R2.frameNStart = frameN;  // exact frame index
      
      R2.setAutoDraw(true);
    }
    
    
    // *rew1* updates
    if (t >= 0.0 && rew1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew1.tStart = t;  // (not accounting for frame time here)
      rew1.frameNStart = frameN;  // exact frame index
      
      rew1.setAutoDraw(true);
    }
    
    
    if (rew2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew2.setText(w2, false);
    }
    
    // *rew2* updates
    if (t >= 0.0 && rew2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew2.tStart = t;  // (not accounting for frame time here)
      rew2.frameNStart = frameN;  // exact frame index
      
      rew2.setAutoDraw(true);
    }
    
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    
    // *plan1_response* updates
    if (t >= 0.0 && plan1_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plan1_response.tStart = t;  // (not accounting for frame time here)
      plan1_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { plan1_response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { plan1_response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { plan1_response.clearEvents(); });
    }
    
    if (plan1_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = plan1_response.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _plan1_response_allKeys = _plan1_response_allKeys.concat(theseKeys);
      if (_plan1_response_allKeys.length > 0) {
        plan1_response.keys = _plan1_response_allKeys[_plan1_response_allKeys.length - 1].name;  // just the last key pressed
        plan1_response.rt = _plan1_response_allKeys[_plan1_response_allKeys.length - 1].rt;
        plan1_response.duration = _plan1_response_allKeys[_plan1_response_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *babyleft* updates
    if (t >= 0.0 && babyleft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      babyleft.tStart = t;  // (not accounting for frame time here)
      babyleft.frameNStart = frameN;  // exact frame index
      
      babyleft.setAutoDraw(true);
    }
    
    
    // *toothbrushright* updates
    if (t >= 0.0 && toothbrushright.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      toothbrushright.tStart = t;  // (not accounting for frame time here)
      toothbrushright.frameNStart = frameN;  // exact frame index
      
      toothbrushright.setAutoDraw(true);
    }
    
    
    // *text_117* updates
    if (t >= 0.0 && text_117.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_117.tStart = t;  // (not accounting for frame time here)
      text_117.frameNStart = frameN;  // exact frame index
      
      text_117.setAutoDraw(true);
    }
    
    
    // *text_120* updates
    if (t >= 0.0 && text_120.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_120.tStart = t;  // (not accounting for frame time here)
      text_120.frameNStart = frameN;  // exact frame index
      
      text_120.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    plan1_info_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function plan1_info_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'plan1_info_2' ---
    plan1_info_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('plan1_info_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(plan1_response.corr, level);
    }
    psychoJS.experiment.addData('plan1_response.keys', plan1_response.keys);
    if (typeof plan1_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('plan1_response.rt', plan1_response.rt);
        psychoJS.experiment.addData('plan1_response.duration', plan1_response.duration);
        routineTimer.reset();
        }
    
    plan1_response.stop();
    // the Routine "plan1_info_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var x;
var _plan2_response_allKeys;
var plan2_infoComponents;
function plan2_infoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'plan2_info' ---
    t = 0;
    plan2_infoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('plan2_info.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_7
    if ((plan1_response.keys === "space")) {
        total_planning += 100;
        if ((Math.random() > 0.5)) {
            x = "baby";
        } else {
            x = "toothbrush";
        }
    } else {
        if ((plan1_response.keys === "left")) {
            x = "baby";
        } else {
            if ((plan1_response.keys === "right")) {
                x = "toothbrush";
            }
        }
    }
    current_image = (("images/" + x) + ".png");
    
    R1_2.setImage('images/computer.png');
    R2_2.setImage(r2);
    plan2_response.keys = undefined;
    plan2_response.rt = undefined;
    _plan2_response_allKeys = [];
    current_image_decision2.setImage(current_image);
    text_118.setText(total_planning);
    // keep track of which components have finished
    plan2_infoComponents = [];
    plan2_infoComponents.push(text_7);
    plan2_infoComponents.push(R1_2);
    plan2_infoComponents.push(R2_2);
    plan2_infoComponents.push(rew1_2);
    plan2_infoComponents.push(rew2_2);
    plan2_infoComponents.push(text_10);
    plan2_infoComponents.push(plan2_response);
    plan2_infoComponents.push(current_image_decision2);
    plan2_infoComponents.push(text_118);
    plan2_infoComponents.push(text_121);
    
    plan2_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function plan2_infoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'plan2_info' ---
    // get current time
    t = plan2_infoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }
    
    
    // *R1_2* updates
    if (t >= 0.0 && R1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R1_2.tStart = t;  // (not accounting for frame time here)
      R1_2.frameNStart = frameN;  // exact frame index
      
      R1_2.setAutoDraw(true);
    }
    
    
    // *R2_2* updates
    if (t >= 0.0 && R2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_2.tStart = t;  // (not accounting for frame time here)
      R2_2.frameNStart = frameN;  // exact frame index
      
      R2_2.setAutoDraw(true);
    }
    
    
    // *rew1_2* updates
    if (t >= 0.0 && rew1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew1_2.tStart = t;  // (not accounting for frame time here)
      rew1_2.frameNStart = frameN;  // exact frame index
      
      rew1_2.setAutoDraw(true);
    }
    
    
    if (rew2_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew2_2.setText(w2, false);
    }
    
    // *rew2_2* updates
    if (t >= 0.0 && rew2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew2_2.tStart = t;  // (not accounting for frame time here)
      rew2_2.frameNStart = frameN;  // exact frame index
      
      rew2_2.setAutoDraw(true);
    }
    
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }
    
    
    // *plan2_response* updates
    if (t >= 0.0 && plan2_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plan2_response.tStart = t;  // (not accounting for frame time here)
      plan2_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { plan2_response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { plan2_response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { plan2_response.clearEvents(); });
    }
    
    if (plan2_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = plan2_response.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _plan2_response_allKeys = _plan2_response_allKeys.concat(theseKeys);
      if (_plan2_response_allKeys.length > 0) {
        plan2_response.keys = _plan2_response_allKeys[_plan2_response_allKeys.length - 1].name;  // just the last key pressed
        plan2_response.rt = _plan2_response_allKeys[_plan2_response_allKeys.length - 1].rt;
        plan2_response.duration = _plan2_response_allKeys[_plan2_response_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *current_image_decision2* updates
    if (t >= 0.0 && current_image_decision2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      current_image_decision2.tStart = t;  // (not accounting for frame time here)
      current_image_decision2.frameNStart = frameN;  // exact frame index
      
      current_image_decision2.setAutoDraw(true);
    }
    
    
    // *text_118* updates
    if (t >= 0.0 && text_118.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_118.tStart = t;  // (not accounting for frame time here)
      text_118.frameNStart = frameN;  // exact frame index
      
      text_118.setAutoDraw(true);
    }
    
    
    // *text_121* updates
    if (t >= 0.0 && text_121.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_121.tStart = t;  // (not accounting for frame time here)
      text_121.frameNStart = frameN;  // exact frame index
      
      text_121.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    plan2_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function plan2_infoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'plan2_info' ---
    plan2_infoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('plan2_info.stopped', globalClock.getTime());
    psychoJS.experiment.addData("image_arrived", current_image);
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(plan2_response.corr, level);
    }
    psychoJS.experiment.addData('plan2_response.keys', plan2_response.keys);
    if (typeof plan2_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('plan2_response.rt', plan2_response.rt);
        psychoJS.experiment.addData('plan2_response.duration', plan2_response.duration);
        routineTimer.reset();
        }
    
    plan2_response.stop();
    // the Routine "plan2_info" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _plan3_response_allKeys;
var plan3_infoComponents;
function plan3_infoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'plan3_info' ---
    t = 0;
    plan3_infoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('plan3_info.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_9
    if ((plan2_response.keys === "space")) {
        total_planning += 100;
        if ((Math.random() > 0.5)) {
            x = "left";
        } else {
            x = "right";
        }
    } else {
        if ((plan2_response.keys === "left")) {
            x = "left";
        } else {
            if ((plan2_response.keys === "right")) {
                x = "right";
            }
        }
    }
    current_image2 = (("images/" + cogmap[((current_image.slice(7, (- 4)) + "_") + x)]) + ".png");
    
    R2_3.setImage(r2);
    plan3_response.keys = undefined;
    plan3_response.rt = undefined;
    _plan3_response_allKeys = [];
    current_image_decision3.setImage(current_image2);
    text_122.setText(total_planning);
    // keep track of which components have finished
    plan3_infoComponents = [];
    plan3_infoComponents.push(text_14);
    plan3_infoComponents.push(R1_3);
    plan3_infoComponents.push(R2_3);
    plan3_infoComponents.push(rew1_3);
    plan3_infoComponents.push(rew2_3);
    plan3_infoComponents.push(text_15);
    plan3_infoComponents.push(plan3_response);
    plan3_infoComponents.push(current_image_decision3);
    plan3_infoComponents.push(text_122);
    plan3_infoComponents.push(text_123);
    
    plan3_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function plan3_infoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'plan3_info' ---
    // get current time
    t = plan3_infoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_14* updates
    if (t >= 0.0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_14.tStart = t;  // (not accounting for frame time here)
      text_14.frameNStart = frameN;  // exact frame index
      
      text_14.setAutoDraw(true);
    }
    
    
    // *R1_3* updates
    if (t >= 0.0 && R1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R1_3.tStart = t;  // (not accounting for frame time here)
      R1_3.frameNStart = frameN;  // exact frame index
      
      R1_3.setAutoDraw(true);
    }
    
    
    // *R2_3* updates
    if (t >= 0.0 && R2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R2_3.tStart = t;  // (not accounting for frame time here)
      R2_3.frameNStart = frameN;  // exact frame index
      
      R2_3.setAutoDraw(true);
    }
    
    
    // *rew1_3* updates
    if (t >= 0.0 && rew1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew1_3.tStart = t;  // (not accounting for frame time here)
      rew1_3.frameNStart = frameN;  // exact frame index
      
      rew1_3.setAutoDraw(true);
    }
    
    
    if (rew2_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rew2_3.setText(w2, false);
    }
    
    // *rew2_3* updates
    if (t >= 0.0 && rew2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rew2_3.tStart = t;  // (not accounting for frame time here)
      rew2_3.frameNStart = frameN;  // exact frame index
      
      rew2_3.setAutoDraw(true);
    }
    
    
    // *text_15* updates
    if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_15.tStart = t;  // (not accounting for frame time here)
      text_15.frameNStart = frameN;  // exact frame index
      
      text_15.setAutoDraw(true);
    }
    
    
    // *plan3_response* updates
    if (t >= 0.0 && plan3_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plan3_response.tStart = t;  // (not accounting for frame time here)
      plan3_response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { plan3_response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { plan3_response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { plan3_response.clearEvents(); });
    }
    
    if (plan3_response.status === PsychoJS.Status.STARTED) {
      let theseKeys = plan3_response.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _plan3_response_allKeys = _plan3_response_allKeys.concat(theseKeys);
      if (_plan3_response_allKeys.length > 0) {
        plan3_response.keys = _plan3_response_allKeys[_plan3_response_allKeys.length - 1].name;  // just the last key pressed
        plan3_response.rt = _plan3_response_allKeys[_plan3_response_allKeys.length - 1].rt;
        plan3_response.duration = _plan3_response_allKeys[_plan3_response_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *current_image_decision3* updates
    if (t >= 0.0 && current_image_decision3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      current_image_decision3.tStart = t;  // (not accounting for frame time here)
      current_image_decision3.frameNStart = frameN;  // exact frame index
      
      current_image_decision3.setAutoDraw(true);
    }
    
    
    // *text_122* updates
    if (t >= 0.0 && text_122.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_122.tStart = t;  // (not accounting for frame time here)
      text_122.frameNStart = frameN;  // exact frame index
      
      text_122.setAutoDraw(true);
    }
    
    
    // *text_123* updates
    if (t >= 0.0 && text_123.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_123.tStart = t;  // (not accounting for frame time here)
      text_123.frameNStart = frameN;  // exact frame index
      
      text_123.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    plan3_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function plan3_infoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'plan3_info' ---
    plan3_infoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('plan3_info.stopped', globalClock.getTime());
    psychoJS.experiment.addData("image_arrived2", current_image2);
    
    if ((plan3_response.keys === "space")) {
        total_planning += 100;
        if ((Math.random() > 0.5)) {
            x = "left";
        } else {
            x = "right";
        }
    } else {
        if ((plan3_response.keys === "left")) {
            x = "left";
        } else {
            if ((plan3_response.keys === "right")) {
                x = "right";
            }
        }
    }
    current_image3 = (("images/" + cogmap[((current_image2.slice(7, (- 4)) + "_") + x)]) + ".png");
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(plan3_response.corr, level);
    }
    psychoJS.experiment.addData('plan3_response.keys', plan3_response.keys);
    if (typeof plan3_response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('plan3_response.rt', plan3_response.rt);
        psychoJS.experiment.addData('plan3_response.duration', plan3_response.duration);
        routineTimer.reset();
        }
    
    plan3_response.stop();
    // the Routine "plan3_info" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var planning4Components;
function planning4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'planning4' ---
    t = 0;
    planning4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('planning4.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_25
    if ((current_image3 === r2)) {
        total_planning += w2;
    }
    psychoJS.experiment.addData("image_arrived3", current_image3);
    
    image_4.setImage(current_image3);
    text_119.setText(total_planning);
    // keep track of which components have finished
    planning4Components = [];
    planning4Components.push(image_4);
    planning4Components.push(text_19);
    planning4Components.push(text_119);
    planning4Components.push(text_131);
    
    planning4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function planning4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'planning4' ---
    // get current time
    t = planning4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_4.setAutoDraw(false);
    }
    
    // *text_19* updates
    if (t >= 0.0 && text_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_19.tStart = t;  // (not accounting for frame time here)
      text_19.frameNStart = frameN;  // exact frame index
      
      text_19.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_19.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_19.setAutoDraw(false);
    }
    
    // *text_119* updates
    if (t >= 0.0 && text_119.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_119.tStart = t;  // (not accounting for frame time here)
      text_119.frameNStart = frameN;  // exact frame index
      
      text_119.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_119.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_119.setAutoDraw(false);
    }
    
    // *text_131* updates
    if (t >= 0.0 && text_131.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_131.tStart = t;  // (not accounting for frame time here)
      text_131.frameNStart = frameN;  // exact frame index
      
      text_131.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_131.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_131.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    planning4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function planning4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'planning4' ---
    planning4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('planning4.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text_20);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_20* updates
    if (t >= 0.0 && text_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_20.tStart = t;  // (not accounting for frame time here)
      text_20.frameNStart = frameN;  // exact frame index
      
      text_20.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_20.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_20.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
