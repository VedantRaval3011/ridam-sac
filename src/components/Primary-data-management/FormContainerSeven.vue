<template>
  <div class="form-container-seven mb-40">
    <div class="bottom-layer">
      <div class="steps">
        <span class="bg-gradient-to-r from-blue-100 to-blue-100 p-3.5 py-2 rounded-xl">8</span> of <span id="total-steps">12</span>
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
    <div class="flex flex-col w-full gap-5 text-center rounded-3xl drop-shadow-md backdrop-blur box-border p-7 bg-gradient-to-r from-blue-100 to-blue-100 container white">
      <div class=" font-semibold">
        <h3>Citation</h3>
      </div>
      <div class="data-prepared-by">
        <label for="dpb" >Data Prepared by </label><br />
        <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="dpb" @input="Validatedpb" />
        <i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="Correctdpb && dpb"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!Correctdpb && dpb"
        ></i>
      </div>
      <div class="original-source">
        <label for="ogsc" class="og">Original Source</label> <br />
        <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="ogsc" @input="ValidateOgsc" /><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectOgsc && ogsc"
        ></i>
        <i
          id="tick"
          class="fa-solid fa-circle-check"
          v-if="!CorrectOgsc && ogsc"
        ></i>
      </div>

      <div class="row">
        <div class="source-scale">
          <label for="source-scale">Source Scale</label><br />
          <input type="text" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="SourceScale" @input="ValidateSourceScale"/><i
            class="fa-solid fa-circle-check"
            id="tick"
            v-if="CorrectSourceScale && SourceScale"
          ></i>
          <i
            id="cross"
            class="fa-solid fa-circle-xmark"
            v-if="!CorrectSourceScale && SourceScale"
          ></i>
        </div>
        <div class="source-date">
          <label for="source-date">Source Date</label><br />
          <input type="date" class="w-44 h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4  box-border" v-model="SourceDate"/>
        </div>
      </div>

      <div class="Lineage">
        <label for="Lineage" class="heading-Lineage">Lineage</label><br />
        <input
          type="text"
          class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border"
          v-model="Lineage"
          @input="ValidateLineage"
        /><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectLineage && Lineage"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectLineage && Lineage"
        ></i>
      </div>
      <div class="coorperate-name">
        <label for="cn" class="heading-cn">Corporate Name</label><br />
        <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="cn" @input="ValidateCn" /><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectCn && cn"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectCn && cn"
        ></i>
      </div>
      <div class="coorperate-address">
        <label for="ad" class="heading-ad">Corporate Address</label><br />
        <input type="text" class="w-full h-10 rounded-3xl bg-blue-50 shadow-md border-none text-base p-4 pr-11 box-border" v-model="ad" @input="ValidateAd" /><i
          class="fa-solid fa-circle-check"
          id="tick"
          v-if="CorrectAd && ad"
        ></i>
        <i
          id="cross"
          class="fa-solid fa-circle-xmark"
          v-if="!CorrectAd && ad"
        ></i>
      </div>
    </div>
    
    
  </div>
</template>

<script>
import { ref, watch } from "vue";
import useValidate from "@vuelidate/core";

export default {
  setup(props, { emit }) {
  const dpb = ref("");
  const Correctdpb = ref(false);
   const ogsc = ref("");
  const CorrectOgsc = ref(false);
  const CorrectSourceScale = ref(false);
  const SourceScale = ref("");
  const SourceDate = ref("");
  const Lineage = ref("");
  const CorrectLineage = ref(false);
  const cn = ref("");
  const CorrectCn = ref(false);
  const ad = ref("");
  const CorrectAd = ref(false);
  const v$ = useValidate();

  

  const Validatedpb = () => {
    Correctdpb.value = dpb.value.length < 50 && dpb.value.length > 3;
  };

  watch(dpb, () => {
    Validatedpb();
  });

   const ValidateOgsc = () => {
    CorrectOgsc.value = ogsc.value.length > 3 && ogsc.value.length < 50;
    console.log(CorrectOgsc.value);
  };

  watch(ogsc, () => {
    ValidateOgsc();
  });

  

  const ValidateSourceScale = () => {
    CorrectSourceScale.value = SourceScale.value.length < 100;
  };

  watch(SourceScale, () => {
    ValidateSourceScale();
  });

  const ValidateLineage = () => {
    CorrectLineage.value = Lineage.value.length < 150;
  };

  watch(Lineage, () => {
    ValidateLineage();
  });

  const ValidateCn = () => {
    CorrectCn.value = cn.value.length < 150;
  };

  watch(cn, () => {
    ValidateCn();
  });

  const ValidateAd = () => {
    CorrectAd.value = ad.value.length < 150;
  };

  watch(ad, () => {
    ValidateAd();
  });

const handleLeftClick = () =>{
    emit('MoveBackToSix');
    console.log("emitting donee");
  };
  const handleRightClick = () => {
    console.log("dpb:", dpb.value, "Correctdpb:", Correctdpb.value);
  console.log("ogsc:", ogsc.value, "CorrectOgsc:", CorrectOgsc.value);
  console.log("SourceScale:", SourceScale.value, "CorrectSourceScale:", CorrectSourceScale.value);
  console.log("SourceDate:", SourceDate.value);
  console.log("Lineage:", Lineage.value, "CorrectLineage:", CorrectLineage.value);
  console.log("cn:", cn.value, "CorrectCn:", CorrectCn.value);
  console.log("ad:", ad.value, "CorrectAd:", CorrectAd.value);
    
      const data = {
        dpb: dpb.value,
        Correctdpb: Correctdpb.value,
        ogsc: ogsc.value,
        CorrectOgsc: CorrectOgsc.value,
        CorrectSourceScale: CorrectSourceScale.value,
        SourceScale: SourceScale.value,
        SourceDate: SourceDate.value,
        Lineage: Lineage.value,
        CorrectLineage: CorrectLineage.value,
        cn: cn.value,
        CorrectCn: CorrectCn.value,
        ad: ad.value,
        CorrectAd: CorrectAd.value,
      };

      emit("update-data", data);

      emit('validate-and-proceed-form-seven');  
    
  };

  return {
    Validatedpb,
    dpb,
    Correctdpb,
    ValidateOgsc,
    ogsc,
    CorrectSourceScale,
    SourceScale,
    SourceDate,
    Lineage,
    CorrectLineage,
    CorrectCn,
    CorrectAd,
    ad,
    cn,
    v$,
    handleRightClick,
    handleLeftClick,
  };
}


}


  

    

</script>

<style scoped>
body {
  padding: 0;
  margin: 0;
}

.data-prepared-by,.original-source,.source-scale,.Lineage,.coorperate-name,.coorperate-address{
  position: relative;
}

.bottom-layer {
  width: 100%;
  padding: 0.5em;
  text-align: center;
  font-size: 1.5rem;
  display: flex;
  gap: 0.3em;
  margin-left: 5em;
}

#right {
  transform: rotate(180deg);
  position: relative;
  left: 0.2em;
}



.row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1em;
}

#tick{
  position: absolute;
  top: 2.2em;
  right: 1em;
  color: green;
}

#cross{
   position: absolute;
  top: 2.2em;
  right: 1em;
  color: crimson;
}
@media screen and (max-width: 640px) {
  /* Small mobile devices */
  .white{
    width: 135%;
  }
  .form-container-seven{
    margin-left: 4.5rem;
  }

  .bottom-layer{
    margin-left: 3em;
  }
  .row{
    flex-direction: column;
  }

  .source-scale input{
    width: 100%;
  }
  .source-date{
    width: 100%;
  }
  .source-date input{
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
