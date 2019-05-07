import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITaskList, ITask} from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {
  public logged = false;
  public username = '';
  public password = '';
  public name: any = '';
  public taskLists: ITaskList[] = [];
  public currentList: ITask[] = [];
  public add = false;
  public taskName = '';
  public taskCreatedAt = '';
  public taskDueOn = '';
  public taskStatus = '';
  public curtaskList: ITaskList;
  public searchName = '';
  public searchTaskList: ITaskList;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
    if (this.logged) {
      this.provider.getTaskLists().then(res => {
        this.taskLists = res;
      });
    }
  }
  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      this.currentList = res;
      this.searchTaskList = taskList;
    });
  }
  removeTaskList(taskList: ITaskList) {
    this.provider.removeTaskList(taskList.id).then(res => {
      console.log(`${taskList.name} deleted`);
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
        console.log(this.taskLists);
      });
    });
  }
  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }
  updateTaskList(taskList: ITaskList) {
    this.provider.updateTaskList(taskList).then(res => {
      console.log(taskList.id + 'updated');
    });
  }
  addClicked(taskList: ITaskList) {
    this.curtaskList = taskList;
    this.add = true;
  }
  addTask() {
    if (this.taskName !== '' && this.taskCreatedAt !== '' && this.taskDueOn !== ''
      && this.taskStatus !== '') {
      this.provider.addTask(this.curtaskList, this.taskName, this.taskCreatedAt, this.taskDueOn, this.taskStatus).then( res => {
        this.add = false;
        this.taskName = '';
        this.taskCreatedAt = '';
        this.taskDueOn = '';
        this.taskStatus = '';
      });
    }
  }
  search() {
    this.provider.search(this.searchTaskList, this.searchName).then( res => {
      this.currentList = res;
    });
  }
  auth() {
    if (this.username !== '' && this.password !== '') {
      this.provider.auth(this.username, this.password).then( res => {
        localStorage.setItem('token', res.token);
        this.provider.getTaskLists().then(r => {
          this.taskLists = r;
        });
        console.log('OK');
        this.logged = true;
      });
    }
  }
  logout() {
    this.provider.logout().then( res => {
      localStorage.clear();
      this.logged = false;
    });
  }

}
