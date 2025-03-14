# Expo Server
[Back](README.md)

1. ```npx expo start```
2. ```npm start``` fails on WSL2 due to network; therefore ```npm start -- --tunnel``` [ref](https://stackoverflow.com/questions/73311889/unable-to-connect-to-expo-react-native-project-on-wsl2-with-expo-go-on-phone)
3. Which fails due to install, so ```npm install @expo/ngrok@2.4.3``` [ref](https://stackoverflow.com/questions/66766591/expo-error-starting-tunnel-failed-to-install-expo-ngrok2-4-3-globally)

## Cannot connect to a backend running on localhost
[Ref](https://revs.runtime-revolution.com/connecting-react-native-to-localhost-65e7ddf43d02)
Set the URL to ```http://10.0.2.2:8000``` for Android Emulator rather than ```localhost```.
