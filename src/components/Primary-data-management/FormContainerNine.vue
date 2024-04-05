<template>
  <div class="form-container-nine mb-96">
    <div class="bottom-layer">
      <div class="steps">
        <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">10</span> of <span id="total-steps">12</span>
      </div>
      <div class="move-icons">
        <i class="fa-solid fa-circle-chevron-left" @click="handleLeftClick"></i>
        <i
          id="right"
          class="fa-solid fa-circle-chevron-left"
          @click="handleRightClick"
        ></i>
      </div>
    </div>
    <div class="flex flex-col w-full gap-5 text-center rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
      <div class=""><h3 class="font-semibold">Launguage</h3></div>
      <div class="language">
        <label for="bsh" >Language ISO 0639-2Bsh</label>
        <div class="language-input">
          <input
            type="language"
            class="w-80 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
            v-model="language"
            @input="Validatelanguage"
          />
          <i
            v-if="Correctlanguage && language"
            class="fa-solid fa-circle-check"
            id="tick"
          ></i>
          <i
            v-else-if="!Correctlanguage && language"
            class="fa-solid fa-circle-xmark"
            id="cross"
          ></i>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import { ref } from "vue";
import useValidate from "@vuelidate/core";

export default {
  setup(props, { emit }) {
    const v$ = useValidate();
    const language = ref("");
    const Correctlanguage = ref(false);

    const Validatelanguage = () => {
      Correctlanguage.value = language.value.length > 1;
    };

    const handleRightClick = () => {

      const data = {
        language: language.value,
        Correctlanguage: Correctlanguage.value,
      };

      emit("update-data", data);
     
        emit("validate-and-proceed-form-nine");

      
    };

    const handleLeftClick = () =>{
      emit("MoveBackToEight");
      console.log("emittiiing");
    }

    return {
      language,
      v$,
      handleRightClick,
      Validatelanguage,
      Correctlanguage,
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

.language-input {
  position: relative;
}

#tick {
  color: green;
  position: absolute;
  top: 0.7em;
  right: 1em;
}

#cross {
  color: crimson;
  position: absolute;
  top: 0.7em;
  right: 1em;
}

.bottom-layer {
  width: 100%;
  padding: 1rem;
  text-align: center;
  font-size: 1.5rem;
  
  display: flex;
  gap: 0.3em;
  margin-left: 6rem;
}

#right {
  transform: rotate(180deg);
  position: relative;
  left: 5px;
}

.language {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.heading {
  position: relative;
  right: 120px;
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



@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .white{
    width: 125%;
  }
  .form-container-nine{
    margin-left: 4rem;
  }
  .language-input input{
    width: 100%;
  }
  .bottom-layer{
    margin-left: 2em;
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