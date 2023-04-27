<script setup>
import { NButton, NInput, NCard, NSpace, NForm, NGrid, NGridItem, useMessage } from "naive-ui";
import { ref } from "vue";
const tasks = ref([]);
const modelRef = ref({
    name: '',
    note: '',
});
const import_thing = ref('');
if (localStorage.getItem('tasks')) {
    tasks.value = JSON.parse(localStorage.getItem('tasks'));
}
function push() {
    /**
     * Add the current modelRef value to the tasks array and reset modelRef to an object with empty name and note properties.
     */

    tasks.value.push(modelRef.value);
    modelRef.value = {
        name: '',
        note: ''
    };
}
const message = useMessage()
function OnClose(index) {
    tasks.value.splice(index, 1);
}
function save() {
    localStorage.setItem('tasks', JSON.stringify(tasks.value));
    message.success('Saved!');
}
function import_local() {
    tasks.value = JSON.parse(import_thing.value);
    import_thing.value = '';
    message.success('Imported!');
}

function import_web() {
    fetch(import_thing.value).then(res => res.json()).then(data => {
        tasks.value = data;
    }).catch(err => {
        message.error("获取失败！");
        console.log(err);
    })
}
function export_() {
    window.navigator.clipboard.writeText(JSON.stringify(tasks.value)).then(() => {
        message.success('Copied!');
    }).catch(err => {
        message.error(err);
    })
}
// for (let index = 0; index < 10001; index++) {
//     push();
// }
setInterval(save, 60000);
</script>
<template>
    <n-space justify="center">
        <h1 id="task">Task</h1>
    </n-space>
    <n-space vertical>
        <n-grid x-gap="8" :y-gap="8" cols="1 200:2 400:4 ">
            <n-grid-item v-for="(item, index) in tasks" :key="index">
                <n-card class="shadow" :title="item.name" closable @close="OnClose(index)">{{
                    item.note }}</n-card>
            </n-grid-item>
        </n-grid>
        <n-form :model="modelRef">
            <n-space vertical>
                <n-form-item path="name">
                    <n-input v-model:value="modelRef.name" placeholder="name" />
                </n-form-item>
                <n-form-item path="note">
                    <n-input type="textarea" v-model:value="modelRef.note" placeholder="note" />
                </n-form-item>
            </n-space>
        </n-form>
        <n-space justify="center">
            <n-button @click="save">save</n-button>
            <n-button @click="push">push</n-button>
        </n-space>
        <n-space justify="center">
            <n-input v-model:value="import_thing" placeholder="import" />
            <n-button @click="import_local">import</n-button>
            <n-button @click="import_web">import from web</n-button>
            <n-button @click="export_">export</n-button>
        </n-space>
    </n-space>
</template>

<style scoped>
.center {
    text-align: center;
}

.shadow:hover {
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
}

.shadow {
    box-shadow: rgba(100, 100, 111, 0.2) 0px 2px 10px 0px;
}

.bg {
    background-color: #6bc235;
}
</style>