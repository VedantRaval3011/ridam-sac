<template>
  <div class="form-container-four mb-96">
    <div class="bottom-layer">
      <div class="steps">
        <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">5</span> of <span id="total-steps">12</span>
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
      <div class="heading">
        <h3>Geographic Location</h3>
      </div>
      <div class="row">
        <div class="left">
          <label for="Spheroid">Spheroid</label>
          <div class="input-left">
            <input class=" w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" type="text" v-model="spheroid" />
            <i
              class="fa-solid fa-circle-check"
              id="tick-left"
              v-if="CorrectSpheroid && spheroid"
            ></i>
            <i
              id="cross-left"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectSpheroid && spheroid"
            ></i>
          </div>
        </div>
        <div class="right">
          <label for="datum">Datum</label>
          <div class="input-right">
            <input class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" type="text" v-model="datum" />
            <i
              class="fa-solid fa-circle-check"
              id="tick-left"
              v-if="CorrectDatum && datum"
            ></i>
            <i
              id="cross-left"
              class="fa-solid fa-circle-xmark"
              v-if="!CorrectDatum && datum"
            ></i>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import { ref } from "vue";
import useValidate from "@vuelidate/core";
export default {
  setup(prop, { emit }) {
    const spheroid = ref("");
    const CorrectSpheroid = ref(true);
    const datum = ref("");
    const CorrectDatum = ref(true);

    const v$ = useValidate();

    const handleRightClick = () => {
      // const { emit } = getCurrentInstance(); // Access emit function using getCurrentInstance
      // Emit an event to the parent component to validate and proceed
      // Ensure that the necessary data is filled
     
        // Emit an event to the parent component
        // This event is caught in the parent component to proceed to the next step

        const data = {
        
        spheroid: spheroid.value,
        datum: datum.value,
        CorrectDatum: CorrectDatum.value,
        CorrectSpheroid: CorrectSpheroid.value,
        
        
        
      };
      // Emit the 'update-data' event with the updated data
      emit("update-data", data);

        console.log("emiting");
        emit("validate-and-proceed-form-four");
      
    };
    const handleLeftClick = () => {
      emit("MoveBackToThree");
    }

    return {
      v$,
      spheroid,
      datum,
      CorrectDatum,
      CorrectSpheroid,
      handleRightClick,
      handleLeftClick,
    };
  },
};
</script>

<style scoped>
body {
  padding: 0;
  margin: 0;
}

.bottom-layer {
  width: 100%;
  padding: 1rem;
  text-align: center;
  font-size: 25px;
  padding-top: 30px;
  display: flex;
  gap: 15px;
  justify-content: center;
}

#right {
  transform: rotate(180deg);
  position: relative;
  left: 0.2em;
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
  padding: 2rem;
  border: none;
  border-radius: 16px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
}


.row {
  display: flex;
  gap: 2rem ;
}


.input-left,
.input-right {
  position: relative;
}



#tick-left {
  position: absolute;
  bottom: 0.7em;
  color: green;
  right: 0.8em;
}
#cross-left {
  position: absolute;
  bottom: 0.7em;
  color: crimson;
  right: 0.8em;
}

/* Base styles */

/* Styles for small phones (portrait and landscape) */
@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .row{
    flex-direction: column ;
  }
  .heading h3{
    right: 17px;
    font-size: 15px;

  }
  .form-container-four{
    margin-left: 7.5rem;
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
