import { combineReducers } from "redux";
import user from "./user";
import auth from "./auth";
import project from "./project"
export default combineReducers({
  user,
  auth,
  project
});