<template>
  <div class="mb-96">
    <div class="bottom-layer ml-20">
    <div class="steps">
      <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">1</span> of <span id="total-steps">12</span>
    </div>
    <div class="move-icons">
      <i class="fa-solid fa-circle-chevron-left" id="left"></i>
      <i
        id="right"
        class="fa-solid fa-circle-chevron-left"
        @click="handleRightClick"
      ></i>
    </div>
  </div>
  <div class=" flex flex-col gap-5 rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
     
     <div class="flex gap-16 name ">
      <label for="name" class=" text-xl mt-2">Name</label>
      <div class="input-wrapper">
        <input type="text" v-model="name" @input="validateName" class=" nameInput h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" /><i
          id="correct"
          class="fa-solid fa-circle-check"
          v-if="CorrectName && name"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectName && name"
        ></i>
      </div>
    </div>
    <div class="flex gap-14 theme">
      <label class=" text-xl mt-2" for="theme" >Theme</label>
      <select name="theme" id="theme" v-model="theme" class="themeInput h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-2 pr-11 box-border align-middle">
        <option value="T1">
          Generic
        </option>
        <option value="T2">vegitation</option>
        <option value="T3">hydrology</option>
        <option value="T4">environment</option>
        
      </select>
    </div>
    <div class="flex gap-5 subtheme">
      <label for="subtheme" class="text-xl mt-2 ">Subtheme</label>
      <select name="subtheme" class=" subthemeInput h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-2  pr-8 pl-4 align-middle" v-model="subtheme">
        <option value="S1">Generic</option>
        <option value="S2">subtheme1</option>
        <option value="S3">subtheme2</option>
        <option value="S4">subtheme3</option>
      </select>
    </div>
     <div class="flex gap-5 product">
      <label for="productId_id" class=" text-xl mt-2 ">Product Id</label>
      <div class="input-wrapper">
        <input type="text" class="nameInput h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border " v-model="productId" @input="validateproductId" /><i
          id="correct"
          class="fa-solid fa-circle-check"
          v-if="CorrectproductId && productId"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectproductId && productId"
        ></i>
      </div>
    </div>
    <div class="flex gap-6 source">
      <label for="sourcelocation" class=" text-xl mt-2 ">Source<br>Locations</label>
      <div class="input-wrapper">
        <input type="text" class=" w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="sourcelocation" @input="validatesourcelocation" @keydown="handleCommaPress"/><i
          id="correct"
          class="fa-solid fa-circle-check"
          v-if="Correctsourcelocation && sourcelocation"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!Correctsourcelocation && sourcelocation"
        ></i>
      </div>
    </div>
  </div>
  </div>
  
 
</template>

<script>
import { ref,watch } from "vue";
import useValidate from "@vuelidate/core";

export default {
 
  props: ['previousData'],
  setup(props, { emit }) {
    
    const theme = ref("");
    const subtheme = ref("");
    const sourcelocation = ref("");
    const Correctsourcelocation = ref(false);
    const sourceLocationArray = ref([]);
    const CorrectproductId = ref(false);
    const productId = ref("");
    const v$ = useValidate();
    const name = ref("");
    const CorrectName = ref(true);
    function validatesourcelocation() {
      Correctsourcelocation.value = sourcelocation.value.startsWith("/");

    }
    
    // Watch for changes in props.previousData
    watch(() => props.previousData, (newVal, oldVal) => {
      
      if (newVal) {
        name.value = newVal.name;
        
      }
    }, { immediate: true });

    const handleCommaPress = (event) => {
       if (event.key === ",") {
    const values = sourcelocation.value.split(",");
    sourceLocationArray.value = []; // Clear the array before adding new values
    values.forEach((value) => {
      const trimmedValue = value.trim();
      if (trimmedValue) { // Check if the trimmed value is not empty
        sourceLocationArray.value.push(trimmedValue);
      }
    });
    console.log(sourceLocationArray.value);
  }
        
    };

    const handleRightClick = () => {
      //logic for handling ID
      const id = theme.value + subtheme.value + productId.value; 
      console.log("this is id"+ id);

      const themeString = mapThemeToString(theme.value);
      const subthemeString = mapSubthemeToString(subtheme.value);



      // Emit an event to the parent component
      // This event is caught in the parent component to proceed to the next step
      console.log("emiting");
      console.log("src location:" + sourceLocationArray.value )

      const data = {
        subtheme: subthemeString,
        theme: themeString,
        sourcelocation: sourcelocation.value,
        name: name.value,
        productId : productId.value,
        id : id,
        sourcelocations: sourceLocationArray.value,
      };
      // Emit the 'update-data' event with the updated data
      emit("update-data", data);
      console.log(id);
    
      emit("validate-and-proceed", subtheme.value, theme.value, sourcelocation.value, productId.value, name.value);

      console.log(themeString);
    };

    const validateproductId = ()=>{
       CorrectproductId.value = productId.value.length < 50 && productId.value.length > 2;
    }

    const mapThemeToString = (themeValue) => {
      switch (themeValue) {
        case "T1":
          return "Generic";
        case "T2":
          return "Vegitation";
        case "T3":
          return "Hydrology";
        case "T4":
          return "Environment";
        default:
          return "";
      }
    };

    const mapSubthemeToString = (subthemeValue) => {
      switch (subthemeValue) {
        case "S1":
          return "Generic";
        case "S2":
          return "Subtheme1";
        case "S3":
          return "Subtheme2";
        case "S4":
          return "Subtheme3";
        default:
          return "";
      }
    };

    return {
      theme,
      subtheme,
      sourcelocation,
      CorrectName,
      Correctsourcelocation,
      validatesourcelocation,
      handleRightClick,
      CorrectproductId,
      productId,
      validateproductId,
      name,
      v$,
     
      handleCommaPress,
    };
  },
};
</script>

<style scoped>

.subthemeInput{
  width: 100%;

}
.white{
  width: 150%;
}

.nameInput{
  width: 100%;
}
.themeInput{
  width: 100%;
}
body {
  margin: 0;
  padding: 0;
  height: 100%;
}


.input-wrapper{
  position: relative;
}

#correct {
  color: green;
  position: absolute;
  z-index: 999;
  font-size: 18px;
  right: 2%;
  margin-top: 12px;
  
}

#cross {
  color: crimson;
  position: absolute;
  z-index: 999;
  font-size: 18px;
  right: 2%;
  margin-top: 12px;
}

#left {
  opacity: 0.8;
}

.bottom-layer {
  width: 100%;
  padding: 1.3rem;
  font-size: 1.5rem;
  display: flex;
  gap: 0.5em;
  justify-content: center;
  text-align: center;
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

#right {
  transform: rotate(180deg);
  position: relative;
  left: 0.1em;
}



/* Base styles */

/* Styles for small phones (portrait and landscape) */
@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .white{
    width: 140%;
    margin-right: 25%;
    gap: 0.2rem;
  }

  .source,.name,.theme,.subtheme,.product{
    flex-direction: column;
    gap: 0;
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
