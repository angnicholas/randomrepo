import React, { useEffect, useState } from 'react';
import CircularProgress from "@mui/material/CircularProgress";
import { getProtected } from "../services/requests";

const ProtectedPage = (props) => {
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getProtected(setContent, setLoading);
  }, []);

  return (
    <>
    {loading === true ? (
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
        }}
      >
        {/* <Backdrop sx={{ color: "grey" }} open={true} /> */}
        <CircularProgress />
      </div>
    ) : (
      <div><p>{content}</p></div>
    )}
    </>
  );
}

export default ProtectedPage;