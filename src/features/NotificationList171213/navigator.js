import { createStackNavigator } from "react-navigation-stack";

import Notifications from "./screens/notifications";
import Home from "./screens";

export default NotificationsBlueprintNavigator = createStackNavigator(
  {
    Home: { screen: Home },
    Notifications: { screen: Notifications },
  },
  {
    initialRouteName: "Home"
  }
);
