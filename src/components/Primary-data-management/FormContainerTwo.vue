<template>
  <div class="form-container-two">
    <div class="bottom-layer">
    <div class="steps">
      <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">3</span> of <span id="total-steps">12</span>
    </div>
    <div class="move-icons">
      <i class="fa-solid fa-circle-chevron-left" id="left" @click="handleLeftClick"></i>
      <i
        id="right"
        class="fa-solid fa-circle-chevron-left"
        @click="handleRightClick"
      ></i>
    </div>
  </div>
    <div class="flex flex-col w-full gap-5 rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
      <div class=""><h3>Data Identification Information</h3></div>
     <div class="bc flex justify-start">
       <div class="">
        <label for="nom" class="">Name of Dataset</label><br />
        <div class="name_of_dataset">
          <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" :value="subtheme" readonly /><i
            class="fa-solid fa-circle-check "
            id="tick-nom"
          ></i>
        </div>
      </div>
     </div>
      <div class=" bc flex justify-start items-start">
        <div class="theme">
        <label for="theme" class="" >Theme</label><br />
        <div class="themeClass">
          <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" :value="theme" readonly /><i
          class="fa-solid fa-circle-check"
          id="tick-theme"
        ></i>
        </div>
      </div>
      </div>
      <div class="flex justify-start">
        <div class="keywords w-full">
        <label class="">Keywords</label> <br />
        <div class="boxes">
          <div class="keyword-row">
            <div
              v-for="(keyword, index) in firstRowKeywords"
              :key="index"
              class="keyword-box"
            >
              <input
                type="text"
                v-model="keyword.value"
                class="pill h-10 w-full rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-6 box-border"
                @input="checkDuplicate(keyword, index, 'firstRowKeywords')"
              />
              <i v-if="keyword.value && !keyword.duplicate" class="fa-solid fa-circle-check valid"></i>
              <i v-else-if="keyword.value && keyword.duplicate" class="fa-solid fa-circle-xmark invalid"></i>
            </div>
          </div>
          <div class="keyword-row">
            <div
              v-for="(keyword, index) in secondRowKeywords"
              :key="index"
              class="keyword-box"
            >
              <input
                type="text"
                v-model="keyword.value"
                class=" pill h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
                @input="checkDuplicate(keyword, index, 'secondRowKeywords')"
              />
              <i v-if="keyword.value && !keyword.duplicate" class="fa-solid fa-circle-check valid"></i>
              <i v-else-if="keyword.value && keyword.duplicate" class="fa-solid fa-circle-xmark invalid"></i>
            </div>
          </div>
        </div>
      </div>
      </div>
      <div class=" acc">
        <div class=" flex flex-col">
        <label for="ac-cs" class="">Access Constraints</label>
        <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="AccessConstraint" @input="ValidateAccessConstraints"/>
        <i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectAccessConstraints && AccessConstraint"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectAccessConstraints && AccessConstraint"
        ></i>
      </div>
      </div>
      <div class="  "> 
        <div class="use flex flex-col">
        <label for="use-cs" class="text-center">Use-Constraints</label> 
        <input type="text" class=" w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="UseConstraints" @input="ValidateUseConstraints"/><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectUseConstraints && UseConstraints"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectUseConstraints && UseConstraints"
        ></i>
      </div>
      </div>
      <div class="">
        <div class="pur flex flex-col">
        <label for="purpose" class="mr-5"
          >Purpose of creating data</label
        >
        <input type="text" class="pc w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="Purpose" @input="ValidatePurpose" /><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectPurpose && Purpose"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectPurpose && Purpose"
        ></i>
      </div>
      </div>
      <div class="bottom">
        <div class="data-type">
          <label for="dataType">Data Type</label><br />
          <select name="data-type" id="dataType" v-model="dataType" class="w-36 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base px-3 box-border align-middle">
            <option value="Vector_Data">Vector Data</option>
            <option value="Raster_Data">Raster Data</option>
          </select>
        </div>
        <div class="Edition">
          <label for="edition">Edition</label><br />
          <select name="edition" id="edition" v-model="edition" class="w-36 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base px-4  box-border align-middle">
            <option value="first">First</option>
            <option value="second">Second</option>
          </select>
        </div>
        <div class="Status">
          <label for="status">Status</label><br />
          <select name="status" id="status" v-model="status" class="w-36 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base px-2  box-border align-middle">
            <option value="completed">Completed</option>
            <option value="in progress">In Progress</option>
          </select>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import { ref, watch } from "vue";
import useValidate from "@vuelidate/core";

export default {
  props: ["subtheme", "theme"],
  setup(props, { emit }) {
    
    const CorrectNameOfDataset = ref(true);
    const firstRowKeywords = ref([
      { value: "", duplicate: false },
      { value: "", duplicate: false },
      { value: "", duplicate: false },
      { value: "", duplicate: false },
    ]);

    const secondRowKeywords = ref([
      { value: "", duplicate: false },
      { value: "", duplicate: false },
      { value: "", duplicate: false },
      { value: "", duplicate: false },
    ]);

    // const CorrectTheme = ref(true);
  
    // const CorrectKeywordOne = ref(false);
    // const KeywordOne = ref("");
    // const CorrectKeywordTwo = ref(true);
    // const KeywordTwo = ref("");
    // const CorrectKeywordThree = ref(true);
    // const KeywordThree = ref("");
    // const CorrectKeywordFour = ref(true);
    // const KeywordFour = ref("");
    // const CorrectKeywordOneOne = ref(true);
    // const KeywordOneOne = ref("");
    // const CorrectKeywordOneTwo = ref(true);
    // const KeywordOneTwo = ref("");
    // const CorrectKeywordOneThree = ref(true);
    // const KeywordOneThree = ref("");
    // const CorrectKeywordOneFour = ref(true);
    // const KeywordOneFour = ref("");
    const status = ref("");
    const edition = ref("");
    const dataType = ref("");
    const CorrectAccessConstraints = ref(false);
    const AccessConstraint = ref("");
    const v$ = useValidate();
    const CorrectUseConstraints = ref(false);
    const UseConstraints = ref("");
    const CorrectPurpose = ref(false);
    const Purpose = ref("");

    const handleRightClick = () => {
      // const { emit } = getCurrentInstance(); // Access emit function using getCurrentInstance
      // Emit an event to the parent component to validate and proceed
      // Ensure that the necessary data is filled
     
        // Emit an event to the parent component
        // This event is caught in the parent component to proceed to the next step

        const data = {
        
        AccessConstraint: AccessConstraint.value,
        CorrectAccessConstraints: CorrectAccessConstraints.value,
        UseConstraints: UseConstraints.value,
        CorrectUseConstraints: CorrectUseConstraints.value,
        Purpose: Purpose.value,
        CorrectPurpose: CorrectPurpose.value,
        firstRowKeywords: firstRowKeywords.value,
        secondRowKeywords: secondRowKeywords.value,
        dataType: dataType.value,
        edition: edition.value,
        status: status.value,
        
        
      };
      // Emit the 'update-data' event with the updated data
      emit("update-data", data);

        emit('validate-and-proceed-second-form');
        console.log('emiteed');
       
      
    };
    
    const handleLeftClick = () =>{
      emit('MoveBackToExtra')
    }

    //Check Access COnstraint Length is < 100
    const ValidateAccessConstraints= ()=>{
      CorrectAccessConstraints.value = AccessConstraint.value.length < 100;
    } 

    // Watch for changes in AccessConstraint
    watch(AccessConstraint, () => {
      ValidateAccessConstraints();
    });
    

    //Check USe COnstraint Length is < 100
    const ValidateUseConstraints= ()=>{
      CorrectUseConstraints.value = UseConstraints.value.length < 100;
    } 
    
    // Watch for changes in USeConstraint
    watch(UseConstraints, () => {
      ValidateUseConstraints();
    });

    //Check Access COnstraint Length is < 100
    const ValidatePurpose= ()=>{
      CorrectPurpose.value = Purpose.value.length < 200;
    } 

    // Watch for changes in AccessConstraint
    watch(AccessConstraint, () => {
      ValidateAccessConstraints();
    });
   

    // Function to check for duplicate keywords
    const checkDuplicate = (keyword, rowIndex, rowType) => {
      if (!keyword.value) {
    keyword.duplicate = false; // Reset duplicate flag if input is empty
    return;

    
  }

  const rowKeywords = rowType === 'firstRowKeywords' ? firstRowKeywords.value : secondRowKeywords.value;
  const allKeywords = [...firstRowKeywords.value, ...secondRowKeywords.value];
  const allValues = allKeywords.map(item => item.value.toLowerCase());

  const currentIndex = rowIndex + (rowType === 'secondRowKeywords' ? firstRowKeywords.value.length : 0);
  const currentValue = keyword.value.toLowerCase();
  const isDuplicate = allValues.filter((item, index) => index !== currentIndex && item === currentValue).length > 0;

  keyword.duplicate = isDuplicate;

  // Check for duplicates across both rows
  if (isDuplicate) {
    alert('Keywords must be different.');
  }
    };

    // Return variables to be used in the component
    return {
      
      ValidateAccessConstraints,
      ValidatePurpose,
      checkDuplicate,
      handleLeftClick,
      secondRowKeywords,
      firstRowKeywords,
      CorrectAccessConstraints,
      CorrectUseConstraints,
      CorrectPurpose,
      Purpose,
      AccessConstraint,
      UseConstraints,
      v$,
      status,
      edition,
      dataType,
      handleRightClick, 
    };
  },
};
</script>


<style scoped>
i {
  z-index: 999;
}
.name_of_dataset,.themeClass,.acc,.use,.pur{
  position: relative;
}


.ac{
  width: 185%;
}

body {
  padding: 0;
  margin: 0;
}

.bottom {
  display: flex;
  /* align-items: center; */
  justify-content: space-evenly;
  gap: 1em;
}



.keyword-rows {
  display: flex;
  flex-direction: column;
}

.keyword-row {
  display: flex;
  justify-content: space-between;
}

.keyword-box {
  width: calc(25% - 10px); /* Adjust as needed */
  position: relative;
}

.keyword-box input {
  width: 100%;
}

#tick{
  color: green;
  position: absolute;
  right: 1em;
  margin-top: 2.5em;
}
/* Add styles for valid and invalid icons */
.valid {
  color: green;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  right: 10px;
}

.bottom-layer {
  width: 100%;
  padding: 20px;
  text-align: center;
  font-size: 25px;
  padding-top: 30px;
  display: flex;
  gap: 15px;
  justify-content: center;
}


.invalid {
  color: crimson;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  right: 10px;
}

#tick-theme {
  color: green;
  position: relative;
  right: 2em;
}

#tick-nom {
  margin-top: 1em;
  color: green;
  position: absolute;
  right: 1em;
}

#tick-box-1,
#tick-box-5 {
  color: green;
  position: absolute;
  top: 15px;
  left: 125px;
}
#tick-box-2,
#tick-box-6 {
  color: green;
  position: absolute;
  top: 15px;
  left: 273px;
}
#tick-box-3,
#tick-box-7 {
  color: green;
  position: absolute;
  top: 15px;
  left: 419px;
}
#tick-box-4,
#tick-box-8 {
  color: green;
  position: absolute;
  top: 15px;
  left: 561px;
}

#tick-purpose,



#right {
  transform: rotate(180deg);
  position: relative;
  left: 5px;
}

#cross-1,
#cross-5 {
  color: crimson;
  position: absolute;
  top: 15px;
  left: 125px;
}
#cross-2,
#cross-6 {
  color: crimson;
  position: absolute;
  top: 15px;
  left: 273px;
}
#cross-3,
#cross-7 {
  color: crimson;
  position: absolute;
  top: 15px;
  left: 419px;
}
#cross-4,
#cross-8 {
  color: crimson;
  position: absolute;
  top: 15px;
  left: 561px;
}

#cross-purpose,
#cross-use-cs,
#cross-ac-cs {
  color: crimson;
  position: relative;
  right: 37px;
}

h1 {
  margin: 0;
}
.form-container-two {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-bottom: 100px;
}

.white-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 10px;

  border-radius: 56px;
  background: linear-gradient(
    180deg,
    #b2e2f1,
    rgba(178, 226, 241, 0.5) 99.99%,
    rgba(178, 226, 241, 0)
  );
  box-shadow: 0px 4.4px 4.42px rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(9.18px);
  box-sizing: border-box;
  padding: 35px 27px 37px 25px;
  max-width: 100%;
}

 

.heading {
  position: relative;
  right: 163px;
}

#current-step {
  background: linear-gradient(
    to bottom,
    #b2e2f1,
    #b2e2f1,
    #b2e2f1,
    #b2e2f1,
    #b2e2f1
  ); /* Gradient fill */
  padding: 15px 20px 12px 20px;
  border: none;
  border-radius: 16px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
}



h3{
  padding: 0;
  margin: 0;
  position: relative;
  left: 25px;
  padding-bottom: 12px;
}

.keyword-heading {
  position: relative;
  right: 250px;
}


  


.boxes {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.row-one {
  position: relative;
  right: 16px;
}
.row-two {
  position: relative;
  right: 16px;
}




input,
select {
  margin-top: 5px;
}

/* Base styles */

/* Styles for small phones (portrait and landscape) */
@media screen and (max-width: 640px) {
  /* Small mobile devices */
  input{
    width: 100%;
  }
  .form-container-two{
    margin-left:10% ;
  }
  .white{
    width: 125%;
    margin-left: 21%;
    gap: 0.2rem;
  }

  .bottom-layer{
    margin-left: 6.5rem;
  }
  .bc{
    display: block;
  }

  .boxes{
    flex-direction: row;
  }
  .keyword-row{
    flex-direction: column;
  }

  .keyword-box input{
    width: 100%;
  }
  .ac{
    width: 100%;
  }
  .bottom{
    flex-direction: column;
  }

  select{
    width: 100%;
  }
  

  .keyword-box{
    width: 100%;
  }
  

}

@media screen and (min-width: 641px) and (max-width: 767px) {
  /* Big mobile devices */
 
}

@media screen and (min-width: 768px) and (max-width: 1023px) {
  /* Small laptops and tablets */
 
}

@media screen and (min-width: 1024px) and (max-width: 1279px) {
  /* Big laptops and desktops */
  
}
@media screen and (min-width: 1280px) and (max-width: 1440px) {
  /* Big laptops and desktops */

}
@media screen and (min-width: 1441px) {
  /* Big laptops and desktops */

}



</style>