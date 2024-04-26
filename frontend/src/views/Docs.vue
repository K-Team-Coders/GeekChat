<template>
  <div class="w-full h-full  uppercase">
    <div class="text-center text-activeText py-2 mb-4 w-full bg-slate-100 font-bold font-monster shadow-sm"> 
        Документация OpenAPI
    </div>
    <div class="text-activeText flex flex-col h-full w-full px-28"  v-for="(doc, index) in swagger_services" :key="index"> 
        <div @click="showSwagger(index)" class=" bg-slate-300 h-11 text-activeText rounded-lg my-2  mx-80 shadow-sm flex items-center justify-center font-bold font-monster hover:bg-slate-400 duration-200">
            {{ doc.name }}
        </div>
        <iframe v-if="activeIndex == index && isShow" class="h-[750px] items-center bg-slate-100 shadow-md" :src="doc.url">
        </iframe>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            swagger_services: [
                {
                name: "Переводчик",
                url: `http://${process.env.VUE_APP_TRANSLATE_SERVICE_IP}/docs`
                },
                {
                name: "Преобразование аудио в текст",
                url: `http://${process.env.VUE_APP_AUDIOREC_SERVICE_IP}/docs`
                },
                {
                name: "Преобразование текста в аудио",
                url: `http://${process.env.VUE_APP_TEXT_TO_AUDIO_SERVICE_IP}/docs`
                },
                {
                name: "Распознавание текста на изображении",
                url: `http://${process.env.VUE_APP_OCR_SERVICE_IP}/docs`
                },
                {
                name: "Обнаружение объектов на изображении",
                url: `http://${process.env.VUE_APP_IMAGE_TO_TEXT_SERVICE_IP}/docs`
                },
                {
                name: "Поиск документов",
                url: `http://${process.env.VUE_APP_DOC_SEARCH_IP}/docs`
                },
                {
                name: "Интеллектуальная поисковая строка",
                url: `http://${process.env.VUE_APP_SERVICE_SEARCH_IP}/docs`
                },
            ],
            activeIndex: null,
            isShow: false
        }
    },

    methods: {
        showSwagger(id){
            if(this.activeIndex == id){
                this.isShow = false;
                this.activeIndex = null;
            }
            else{
                this.activeIndex = id;
                this.isShow = true;
            }
            return this.activeIndex
        }
    }
}
</script>

<style>

</style>