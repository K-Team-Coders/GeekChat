<template>
  <div class="container duration-500">
    <div class="large-12 medium-12 small-12 cell">
      <label>File Preview
        <input type="file" id="file" ref="file" accept="image/*" v-on:change="handleFileUpload()"/>
      </label>
      <img v-bind:src="imagePreview" v-show="showPreview"/>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
    data(){
      return {
        file: '',
        showPreview: false,
        imagePreview: ''
      }
    },
    methods: {
      submitFile(){
            let formData = new FormData();
            formData.append('file', this.file);
            axios.post( '/file-preview',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
        let reader  = new FileReader();
        reader.addEventListener("load", function () {
          this.showPreview = true;
          this.imagePreview = reader.result;
        }.bind(this), false);
        if( this.file ){
          if ( /\.(jpe?g|png|gif)$/i.test( this.file.name ) ) {
            reader.readAsDataURL( this.file );
          }
        }
      }
    }
  }
</script>

<style>
  div.container img{
    max-width: 200px;
    max-height: 200px;
  }
</style>