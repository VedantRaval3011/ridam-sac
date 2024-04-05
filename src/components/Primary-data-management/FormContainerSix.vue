<template>

  <div class="form-container-six mb-96">
    <div class="bottom-layer">
      <div class="steps">
        <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">7</span> of <span id="total-steps">12</span>
      </div>
      <div class="move-icons">
        <i
          class="fa-solid fa-circle-chevron-left"
          id="left"
          @click="handleLeftCLick"
        ></i>
        <i
          id="right"
          class="fa-solid fa-circle-chevron-left"
          @click="handleRightClick"
        ></i>
      </div>
    </div>
    <div class="flex flex-col w-96 gap-5 text-center rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
      <div class=""><h3 class=" font-semibold">Metadata Stamp</h3></div>
      <div class="date">
        <label for="metadata-stamp-date">Metadata Stamp Date</label>
        <div class="date-input">
          <input type="date" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4  box-border" v-model="date" />
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
    const date = ref("");

    const handleRightClick = () => {
      // const { emit } = getCurrentInstance(); // Access emit function using getCurrentInstance
      // Emit an event to the parent component to validate and proceed
      // Ensure that the necessary data is filled

      // Emit an event to the parent component
      // This event is caught in the parent component to proceed to the next step

      const data = {
        date: date.value,
      };

      emit("update-data", data);

      console.log("emiting");
      emit("validate-and-proceed-form-six");
    };
    const handleLeftCLick = () => {
      emit("MoveBackToFive");
    };
    return {
      date,
      v$,
      handleRightClick,
      handleLeftCLick,
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
  font-size: 1.5rem;
  display: flex;
  gap: 0.3rem;
  margin-left: 4em;
}

#right {
  transform: rotate(180deg);
  position: relative;
  left: 0.3rem;
}

.date {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .white{
    width: 100%;
  }
  .form-container-six{
    margin-left: 7.5rem;
  }

  .bottom-layer{
    margin-left: 1em;
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