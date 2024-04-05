9<template>
  <div class="form-container-eight mb-96">
    <div class="bottom-layer">
      <div class="steps">
        <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">9</span> of <span id="total-steps">12</span>
      </div>
      <div class="move-icons">
        <i class="fa-solid fa-circle-chevron-left" id="left" @click="handleLeftCLick"></i>
        <i
          id="right"
          class="fa-solid fa-circle-chevron-left"
          @click="handleRightClick"
        ></i>
      </div>
    </div>
    <div class="flex flex-col w-96 gap-5 text-center rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
      <div class="font-semibold"><h3>Data Topic Category</h3></div>
      <div class="DITC">
        <label for="topic-category">Data identification topic category</label>
        <div class="DITC-input">
          <input
            type="DITC"
            class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
            v-model="DITC"
            @input="ValidateDitc"
          />
          <i
            v-if="CorrectDitc && DITC"
            class="fa-solid fa-circle-check"
            id="tick"
          ></i>
          <i
            v-else-if="!CorrectDitc && DITC"
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
    const DITC = ref("");
    const CorrectDitc = ref(false);

    const ValidateDitc = () => {
      CorrectDitc.value = DITC.value.length > 1;
    };

    const handleRightClick = () => {

      const data = {
        DITC: DITC.value,
        
      };

      emit("update-data", data);
      
        emit("validate-and-proceed-form-eight");
      
    };
    const handleLeftCLick= () =>{
      emit("MoveBackToSeven");
    }

    return {
      DITC,
      v$,
      handleRightClick,
      ValidateDitc,
      CorrectDitc,
      handleLeftCLick
    };
  },
};
</script>
<style scoped>
body {
  padding: 0;
  margin: 0;
}



.DITC-input {
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
  padding: 1em;
  text-align: center;
  font-size: 1.5rem;
  display: flex;
  gap: 0.3em;
  margin-left: 2.6em;
}

#right {
  transform: rotate(180deg);
  position: relative;
  left: 0.3em;
}

.DITC {
  display: flex;
  flex-direction: column;
  gap: 1em;
}

@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .white{
    width: 100%;
  }
  .form-container-eight{
    margin-left: 4rem;
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