import { Component, OnInit } from '@angular/core';
import {ITask, ITasklist} from '../shared/models/models';
import {ProviderService} from '../shared/services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public tasklists: ITasklist[] = [];
  public tasks: ITask[] = [];
  public name: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTasklists().then(res => {
      this.tasklists = res;
    });
  }

  getTasks(task: ITasklist) {
    this.provider.getTasks(task).then(res => {
      this.tasks = res;
    });
  }

  updateTaskList(t: ITasklist) {
    this.provider.updateTaskList(t).then(res => {
      console.log(t.name + ' updated');
    });
  }

  deleteTaskList(t: ITasklist) {
    this.provider.deleteTaskList(t.id).then(res => {
      console.log(t.name + ' deleted');
      this.provider.getTasklists().then(r => {
        this.tasklists = r;
      });
    });
  }

  createTask() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.tasklists.push(res);
      });
    }
  }
}
