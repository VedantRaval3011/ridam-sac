<template>
  <div class="extra mb-96">
    <div class="bottom-layer ">
    <div class="steps">
      <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">2</span> of <span id="total-steps">12</span>
    </div>
    <div class="move-icons">
      <i
        class="fa-solid fa-circle-chevron-left"
        id="left"
        @click="handleLeftClick"
      ></i>
      <i
        id="right"
        class="fa-solid fa-circle-chevron-left"
        @click="handleRightClick"
      ></i>
    </div>
  </div>
  <div class="flex flex-col gap-5 rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
    <div class="flex gap-16 extension">
      <label class=" text-xl mt-2" for="extension">Extension</label>
      <select name="extension"  class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-2 pr-11 box-border allign-middle" v-model="extension">
        <option value="jp2">.jp2</option>
        <option value="tif">.tif</option>
      </select>
    </div>
    <div class="flex gap-8 compression">
      <label for="compression" class=" text-xl mt-2">Compression</label>
      <select name="compression"  class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-2 pr-11 box-border" v-model="Compression">
        <option value="jp2000">jp2000</option>
        <option value="deflate">deflate</option>
      </select>
    </div>
    <div class="flex gap-12 resampling">
      <label for="resampling" class=" text-xl mt-2">Resampling</label>
      <select name="compression" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-2 pr-11 box-border" v-model="resampling">
        <option value="Nearest">Nearest</option>
        <option value="Mode">Mode</option>
        <option value="average">Average</option>
      </select>
    </div>
    <div class="flex gap-16 interleave">
      <label for="interleave" class=" text-xl mt-2">Interleave</label>
      <select name="interleave" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-2 pr-11 box-border" v-model="interleave">
        <option value="pixel">Pixel</option>
      </select>
    </div>

    <div class="flex gap-10 projection" >
      <label for="projection" class=" text-xl mr-5 mt-2">Projection</label>
      <div class="flex gap-2 boxes ">
        <div class="first flex">
          <input @input="validateProjections"
            type="text"
            id="projection1"
            class=" w-24 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
            v-model="Projection"
          />
          <i
            class="fa-solid fa-circle-check"
            id="tick"
            v-if="CorrectProjectOne && Projection"
          ></i>
          <i
            id="cross"
            class="fa-solid fa-circle-xmark"
            v-if="!CorrectProjectOne && Projection"
          ></i>
        </div>

        <button class=" add py-2 px-4 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75 mr-56" v-if="!showProjection2" @click="addInput">Add</button>
        <div class="second">
          <input
            type="text"
            id="projection"
            class=" w-24 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
            v-model="Projection2"
            v-show="showProjection2"
          />
          <i
            class="fa-solid fa-circle-check"
            id="tick"
            v-show="CorrectProjectTwo && Projection2"
          ></i>
          <i
            id="cross"
            class="fa-solid fa-circle-xmark"
            v-show="!CorrectProjectTwo && Projection2"
          ></i>
        </div>
        <button class=" add-2 py-2 px-4 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg shadow-md focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75 mr-56" v-show="!showProjection3 && showProjection2" @click="addInput2">
          Add
        </button>
        <div class="third">
          <input
            type="text"
            id="projection"
            class=" w-24 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
            v-model="Projection3"
            v-show="showProjection3"
          />
          <i
            class="fa-solid fa-circle-check"
            id="tick"
            v-show="CorrectProjectThree && Projection3"
          ></i>
          <i
            id="cross"
            class="fa-solid fa-circle-xmark"
            v-show="!CorrectProjectThree && Projection3"
          ></i>
        </div>
      </div>
    </div>
  </div>
  
  <input
    type="hidden"
    :value="subtheme"
    @input="updateSubtheme($event.target.value)"
  />
  <input
    type="hidden"
    :value="theme"
    @input="updateTheme($event.target.value)"
  />
  </div>
</template>

<script>
import { ref, watch } from "vue";
import useValidate from "@vuelidate/core";

export default {
  props: ["subtheme", "theme"],

  setup(props, { emit }) {
    const extension = ref("");
    const interleave = ref("");
    const Compression = ref("");
    const Projection = ref("");
    const Projection2 = ref("");
    const Projection3 = ref("");
    const showProjection3 = ref(false);
    const showProjection2 = ref(false);
    const resampling = ref("");
    const Correctprojections = ref(false); // Initial validation
    const CorrectProjectOne = ref(false);
    const CorrectProjectTwo = ref(false);
    const CorrectProjectThree = ref(false);
    const Projectionarray = ref([]);
    const paused = ref(false);
    const temporal_frequency = ref("daily");
   const validateProjections = () => {
     Projectionarray.value = []; 
  if (Projection.value.trim() !== "") {
    Projectionarray.value.push(Projection.value);
  }
  if (Projection2.value.trim() !== "") {
    Projectionarray.value.push(Projection2.value);
  }
  if (Projection3.value.trim() !== "") {
    Projectionarray.value.push(Projection3.value);
  }
};

    const v$ = useValidate();
    function addInputWrapper() {}

    const addInput = () => {
      showProjection2.value = true;
    };
    
    const addInput2 = () => {
      showProjection3.value = true;
    };

    const updateSubtheme = (value) => {
      this.$emit("update:subtheme", value);
    };
    const updateTheme = (value) => {
      this.$emit("update:theme", value);
    };

    const validateProjection = () => {
      CorrectProjectOne.value =
        Projection.value !== Projection2.value &&
        Projection.value !== Projection3.value;
      CorrectProjectTwo.value =
        Projection2.value !== Projection.value &&
        Projection2.value !== Projection3.value;
      CorrectProjectThree.value =
        Projection3.value !== Projection.value &&
        Projection3.value !== Projection2.value;

      if (
        (!CorrectProjectOne.value ||
          !CorrectProjectTwo.value ||
          !CorrectProjectThree.value) &&
        Projection.value.trim() !== "" &&
        Projection2.value.trim() !== "" &&
        Projection3.value.trim() !== ""
      ) {
        alert(
          "Please ensure that the projections are different from each other."
        );
      }
    };

    watch(Projection, validateProjection);
    watch(Projection2, validateProjection);
    watch(Projection3, validateProjection);

    const handleRightClick = () => {
      
      // Emit an event to the parent component to validate and proceed
      validateProjections();

      // Emit an event to the parent component
      // This event is caught in the parent component to proceed to the next step
      console.log(Projectionarray.value);
     
      emit(
        "validate-and-proceed",
      );
      const data = {
        subtheme: props.subtheme,
        theme: props.theme,
        extension: extension.value,
        Compression: Compression.value,
        Projection: Projection.value,
        Projection2: Projection2.value,
        Projection3: Projection3.value,
        CorrectProjectOne: CorrectProjectOne.value,
        CorrectProjectTwo: CorrectProjectTwo.value,
        CorrectProjectThree: CorrectProjectThree.value,
        resampling: resampling.value,
        interleave: interleave.value,
        projection: Projectionarray.value,
        paused : paused.value,
        temporal_frequency: temporal_frequency.value,
      };
      // Emit the 'update-data' event with the updated data
      emit("update-data", data);
    };

    const handleLeftClick = () => {
      emit("MoveBackToOne");
    };

    return {
      extension,
      handleLeftClick,
      updateSubtheme,
      updateTheme,
      CorrectProjectOne,
      CorrectProjectThree,
      CorrectProjectTwo,
      Projection2,
      Projection3,
      addInput2,
      Compression,
      addInput,
      Projection,
      Correctprojections,
      addInputWrapper,
      showProjection2,
      showProjection3,
      validateProjection,
      handleRightClick,
      v$,
      interleave,
      resampling,
      validateProjections,
      paused,
      temporal_frequency,
    };
  },
};
</script>

<style scoped>

.white{
  width: 32rem; 
}

.projection{
  position: relative;
}

body {
  margin: 0;
  padding: 0;
  height: 100%;
}




#tick {
  color: green;
  position: absolute;
  z-index: 999;
  right: 9px;
  top: 12px;
}

#cross {
  color: crimson;
  position: absolute;
  z-index: 999;
  right: 10px;
  top: 12px;
}



.bottom-layer {
  width: 100%;
  padding: 1em;
  text-align: center;
  font-size: 1.5em;
  
  display: flex;
  gap: 0.5rem;
  justify-content: center;
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
  .bottom-layer{
    margin-left: 4rem;
  }
  .extra{
    margin-left: 4em;
  }
  .white{
    width:115%;
    margin-left: 21%;
    gap: 0.2rem;
    height: 36rem;
    
  }

 
 .interleave,.projection,.extension,.compression,.resampling{
  flex-direction: column;
  gap: 0.2rem;
 }

 .boxes{
  flex-direction: column;
  position: relative;
 }
 .add{
  position: absolute;
  margin-top: 3em;
  width: 5rem;
  margin-left: 5.5rem;
  
  height: 2.5rem;
 }

 #projection{
  width: 100%;
 }

 #projection1{
 width: 100%;
 }

 .projection label{
  margin-left: 11%;
 }

 .add-2{
  position: absolute;
  margin-top: 6em;
  width: 5rem;
  margin-left: 5.5rem;
  height: 2.5rem;
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
