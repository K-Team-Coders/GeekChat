<template>
    <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-screen">
        <div class="fixed w-64 left-6">
            <SidebarMain />
        </div>
        <div
            class="ml-72 w-full outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
            <div class="flex flex-row"> 
                <div class=" w-full px-2 uppercase text-activeText font-monster font-bold  mt-4 text-center text-md">
                    Оценка активности: 65
                </div>
                <div class=" w-full px-2 uppercase text-activeText font-monster font-bold  mt-4 text-center text-md">
                    Оценка настроения: 42
                </div>
            </div>
            <div class="w-full grid grid-cols-3 ">
                <!-- <div class="col-span-3 flex flex-row justify-around mb-2">

                    <MaterialCardVue :icon_name="'chat'" :title="'пользователей'" :value="123" :color="'bg-red-700'" />
                    <MaterialCardVue :icon_name="'chat'" :title="'Проблем'" :value="132"
                        :color="'bg-indigo-500'" />
                    <MaterialCardVue :icon_name="'chat'" :title="'Количество пользователей'" :value="3"
                        :color="'bg-purple-500'" />
                </div> -->

                  
                <div class="h-[60vh] overflow-y-auto p-16 w-full outline-[1px]  mt-2 col-span-2 outline-dashed outline-outlineColor ">
                    <div :class="`${message.from[1]}`" v-for="message in spliceMessages">

                        <div :class="`${message.from[0]}`">
                            <p class="text-orange-200">{{ message.username }}</p>
                            <hr>
                            <p class="text-gray-200">{{ message.message }}</p>
                            <p class="text-gray-200 text-xs w-full text-end">{{ dataFromatter(message.date) }}</p>
                        </div>
                    </div>
                </div>


                <div
                    class=" w-full h-[60vh]  outline-dashed bg-frameBackground mt-2 outline-[1px] outline-outlineColor duration-500">
                    <div class=" p-3">
                        <p class="text-activeText py-2 text-center rounded-xl mb-4 text-xl font-medium duration-500">
                            Эфир обработанных сообщений
                        </p>
                        <input
                            class="w-full rounded-sm h-10 border-[0.1px] bg-transparent px-4 text-activeText placeholder:text-unactiveText border-neutral-500 dark:border-neutral-200 duration-500"
                            type="text" placeholder="Поиск событий" />
                        <div class="w-full overflow-y-scroll custom-scrollbar duration-500">
                            <div v-for="event in dynamicNews" :key="event.id"
                                class="text-activeText pt-2 w-full duration-500 ">
                                <div
                                    class=" px-2 py-2 flex relative items-center hover:bg-slate-300 dark:hover:bg-stone-900  duration-300 transition ease-in-out hover:-translate-y-1 hover:scale-103 bg-slate-200 shadow-xl  outline-dashed dark:bg-background outline-[1.5px] outline-outlineColor ">
                                    <div class="h-full w-full">
                                        <div
                                            class="flex justify-between text-red-600 uppercase font-bold text-xs font-rale">
                                            {{ event.title }}
                                        </div>
                                        <p class="text-xs h-full  text-left whitespace-pre-line break-words font-rale">
                                            {{ event.text }}
                                        </p>
                                        <div
                                            class="text-start dark:text-purple-400 text-purple-600 text-xs font-roboto font-bold">
                                            {{
                                                event.class }}</div>
                                        <div
                                            class="text-end dark:text-orange-400 text-zink-600 text-xs font-roboto font-bold">
                                            {{
                                                dataFromatter(event.date) }}</div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
            <div class="w-full grid grid-cols-2 gap-4 mt-3">
                <LineChartVue />
                <LineChartVue />
            </div>


        </div>
    </div>
</template>
<script>
import axios from 'axios';

import SidebarMain from "./SidebarMain.vue";
import LineChartVue from './charts/LineChart.vue';
export default {
    components: {
       
        SidebarMain,
        LineChartVue

    },

    data() {
        return {
            message: '',
            messages: [],
            sessionID: 1,
            isLoading: false,
            myname: '',
            isError: false,
            isReady: false,
            connection_data: null,
        };
    },

    methods: {
        sendMessage() {
            if (this.message.trim() !== "") {
                this.connection_data.send(this.message);
                console.log("Отправлено:")
                console.log(this.message)
                this.message = "";
            }
        },

        isMessageFromMe(name) {
            switch (name) {
                case "me":
                    return ['max-w-96 bg-indigo-500 text-white rounded-lg p-3 gap-3', 'flex justify-end mb-4 cursor-pointer']
                case "not_me":
                    return ['max-w-96 dark:bg-white bg-slate-200 rounded-lg p-3 h-20 gap-3', 'flex mb-4 cursor-pointer']
            }
        },

        dataFromatter(data) {
            let date = new Date(data);

            // Получаем день, месяц, год, часы, минуты и секунды
            let day = date.getDate();
            let month = date.getMonth() + 1; // Месяцы начинаются с 0, поэтому добавляем 1
            let year = date.getFullYear();
            let hours = date.getHours();
            let minutes = date.getMinutes();
            let seconds = date.getSeconds();

            // Форматируем день, месяц, часы, минуты и секунды, чтобы они были двузначными, если меньше 10
            day = day < 10 ? "0" + day : day;
            month = month < 10 ? "0" + month : month;
            hours = hours < 10 ? "0" + hours : hours;
            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            // Создаем строку в формате "день.месяц.год часы:минуты:секунды"
            let formattedDate = hours + ":" + minutes + ":" + seconds + " " + day + "." + month + "." + year
            return formattedDate
        },
    },

    computed: {
        isDarkMode() {
            return this.$store.state.darkMode;
        },

        spliceMessages() {
            let messages = this.messages;
            messages.forEach((message) => {
                if (message.username == this.myname) {
                    message["from"] = this.isMessageFromMe("me")
                }
                else {
                    message["from"] = this.isMessageFromMe("not_me")
                }
            })
            return messages
        }
    },

    async mounted() {
        this.isLoading = true;
        await axios.get(`http://${process.env.VUE_APP_CHAT_SOCKET_IP}/register`)
            .then((response) => {
                console.log('Токен получен:');
                console.log(response.data);
                const name = response.data.token;
                this.myname = name;
            })

        console.log(this.myname);
        console.log("Подключение к веб-сокету...");
        let connection = new WebSocket(
            `ws://${process.env.VUE_APP_CHAT_SOCKET_IP}/ws/${this.sessionID}/${this.myname}`
        );

        connection.onopen = (event) => {
            console.log(event);
            console.log("Подключение успешно!");
            this.connection_data = connection;
            this.isLoading = false;
        };

        connection.onclose = (event) => {
            if (event.wasClean) {
                console.log(
                    `[close] Соединение закрыто чисто, код=${event.code} причина=${event.reason}`
                );
                this.isLoading = false;
            } else {
                // например, сервер убил процесс или сеть недоступна
                // обычно в этом случае event.code 1006
                console.log("[close] Соединение прервано");
                this.isLoading = false;
            }
        };

        connection.onerror = (error) => {
            console.log(`[error]`);
            this.isLoading = false;
        };

        connection.onmessage = (event) => {
            console.log("Получено:");
            console.log(JSON.parse(event.data));
            let parsed_message = JSON.parse(event.data)
            this.messages.push(parsed_message);
        };
    },
};
</script>
<style>
.rainbows {
    position: relative;
}

@keyframes rainbow {
    0% {
        color: white;
    }

    33% {
        color: blue;
    }

    66% {
        color: red;
    }

    100% {
        color: white;
    }
}

.owl {
    position: absolute;
    width: 40px;
    height: 40px;
    background-image: url("https://freesvg.org/img/1531730612.png");
    background-size: cover;
    animation: fly-around 5s ease-in-out infinite;
}

@keyframes fly-around {
    0% {
        left: 40px;
        top: 0px;
    }

    25% {
        left: 40px;
        top: 20px;
    }

    50% {
        left: 55px;
        top: 5px;
    }

    75% {
        left: 25;
        top: 15px;
    }

    100% {
        left: 40px;
        top: 0px;
    }
}

.custom-scrollbar {
    scrollbar-width: thin;
    scrollbar-color: #535353 #272727;
}

.custom-scrollbar::-webkit-scrollbar {
    width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
    background: #27272700;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
    background-color: #535353;
    border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background-color: #323232;
}
</style>