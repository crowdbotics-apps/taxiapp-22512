import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile171270Navigator from '../features/UserProfile171270/navigator';
import Maps171251Navigator from '../features/Maps171251/navigator';
import Settings171229Navigator from '../features/Settings171229/navigator';
import Settings171214Navigator from '../features/Settings171214/navigator';
import NotificationList171213Navigator from '../features/NotificationList171213/navigator';
import Maps171212Navigator from '../features/Maps171212/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
UserProfile171270: { screen: UserProfile171270Navigator },
Maps171251: { screen: Maps171251Navigator },
Settings171229: { screen: Settings171229Navigator },
Settings171214: { screen: Settings171214Navigator },
NotificationList171213: { screen: NotificationList171213Navigator },
Maps171212: { screen: Maps171212Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
