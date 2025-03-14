import { ConstructionOutlined } from "@mui/icons-material";
import api from "./auth.interceptor";
import { removeUser } from "./auth.tokens";

export const login = async (email, password, setRequestFailed) => {
  await api
    .post("/auth/jwt/login", {
      email,
      password,
    })
    .then((response) => {
      console.log('T6HIS IS THE RESPONSE', response.data);
      if (response.data.access) {
        localStorage.setItem("email", email);
        localStorage.setItem("user", JSON.stringify(response.data));
        // localStorage.setItem("id", response.data.id);
        // localStorage.setItem("role", response.data.role);
        // console.log('local storage', localStorage.getItem("role"));
        // console.log('response data', response.data.role);
        response.data.role === "EU"
          ? window.location.replace("/enduser")
          : window.location.replace("/institution");
      } else {
        window.location.replace("/login");
      }
    })
    .catch((err) => {
      setRequestFailed();
    });
};

export const logout = () => {
  removeUser();
  window.location.replace("/login");
};

export const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem("user"));
};
