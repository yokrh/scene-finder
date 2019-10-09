<template>
  <div class="scene-finder">
    <h1 id="scroll-top">{{ title }}</h1>

    <form method="post"
      :action="`${apiServer}/upload/movie`"
       enctype="multipart/form-data"
    >
      <input type="file" name="video">
      <input type="submit" value="upload">
    </form>

    <div>
      <el-button @click="findScenes">Find</el-button>
    </div>

    <div>
      <el-button
        id="scroll-top-button"
        type="info"
        round
        style="margin:60px auto; padding:12px 40px;"
        @click="scrollTop"
      >
        ↑ トップに戻る
      </el-button>
    </div>
  </div>
</template>

<script>
export default {
  components: [],
  props: [],
  data() {
    return {
      apiServer: 'http://localhost:3000',
      title: 'Scene Finder',
    };
  },
  computed: {},
  mounted() {},
  methods: {
    findScenes() {
      console.log('findScenes');
    },
    scrollTop() {
      document.getElementById('scroll-top').scrollIntoView(false);
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 480px) {
}
</style>
