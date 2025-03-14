import api from "./auth.interceptor";

export async function getProtected(setContent, setLoading){
  await api
    .get("/protected/")
    .then((res) => {
      setContent(res.data);
      setLoading(false);
    })
    .catch((err) => console.log(err));
}